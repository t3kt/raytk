// raytkSdf.glsl

Sdf opSimpleUnion(Sdf res1, Sdf res2){
	return (res1.x<res2.x)? res1:res2;
}

float opSimpleUnion(float res1, float res2) {
	return min(res1, res2);
}

Sdf opSimpleIntersect(Sdf res1, Sdf res2) {
	return (res1.x>res2.x) ? res1 : res2;
}

float opSimpleIntersect(float res1, float res2) {
	return max(res1, res2);
}

Sdf opSimpleDiff(Sdf res1, Sdf res2) {
	Sdf res = res1;
	res.x = max(-res2.x, res1.x);
	return res;
}

float opSimpleDiff(float res1, float res2) {
	return max(-res2, res1);
}

float smoothBlendRatio(float a, float b, float k) {
	return clamp(0.5 + 0.5*(b-a)/k, 0.0, 1.0);
}

float opSmoothIntersect(float res1, float res2, float k) {
	float h = clamp(0.5 - 0.5*(res2-res1)/k, 0., 1.);
	return mix(res2, res1, h) + k*h*(1.0-h);
}

float opSmoothDiff(float res1, float res2, float k) {
	return opSmoothIntersect(res1, -res2, k);
}

Sdf opSmoothIntersect(Sdf res1, Sdf res2, float k) {
	Sdf res = res1;
	float h = clamp(0.5 - 0.5*(res2.x-res1.x)/k, 0., 1.);
	res.x = mix(res2.x, res1.x, h) + k*h*(1.0-h);
	blendInSdf(res1, res2, h);
	return res;
}

Sdf opSmoothUnionM(Sdf res1, Sdf res2, float k) {
	float h = smoothBlendRatio(res1.x, res2.x, k);
	float resx = mix(res2.x, res1.x, h) - k*h*(1.0-h);
	res1.x = resx;
	blendInSdf(res1, res2, 1. - h);
	return res1;
}

float opSmoothUnionM(float d1, float d2, float k) {
	float h = smoothBlendRatio(d1, d2, k);
	return mix(d2, d1, h) - k*h*(1.0-h);
}

float sdTetrahedron(vec3 p) {
	return (
		max(
			max(-p.x-p.y-p.z, p.x+p.y-p.z),
			max(-p.x+p.y+p.z, p.x-p.y+p.z))
		-1.)/sqrt(3.0);
}

float fOpUnionStairs(float a, float b, float r, float n, float o) {
	float s = r/n;
	float u = b-r;
	return min(min(a,b), 0.5 * (u + a + abs ((mod (u - a + s + o, 2 * s)) - s)));
}

// We can just call Union since stairs are symmetric.
float fOpIntersectionStairs(float a, float b, float r, float n, float o) {
	return -fOpUnionStairs(-a, -b, r, n, o);
}

float fOpDifferenceStairs(float a, float b, float r, float n, float o) {
	return -fOpUnionStairs(-a, b, r, n, o);
}

// version with offset
float fOpUnionColumns(float a, float b, float r, float n, float o) {
	if ((a < r) && (b < r)) {
		vec2 p = vec2(a, b);
		float columnradius = r*sqrt(2)/((n-1)*2+sqrt(2));
		pR45(p);
		p.x -= sqrt(2)/2*r;
		p.x += columnradius*sqrt(2);
		if (mod(n,2) == 1) {
			p.y += columnradius;
		}
		// At this point, we have turned 45 degrees and moved at a point on the
		// diagonal that we want to place the columns on.
		// Now, repeat the domain along this direction and place a circle.
		p.y += o;
		pMod1(p.y, columnradius*2);
		float result = length(p) - columnradius;
		result = min(result, p.x);
		result = min(result, a);
		return min(result, b);
	} else {
		return min(a, b);
	}
}

float fOpDifferenceColumns(float a, float b, float r, float n, float o) {
	a = -a;
	float m = min(a, b);
	//avoid the expensive computation where not needed (produces discontinuity though)
	if ((a < r) && (b < r)) {
		vec2 p = vec2(a, b);
		float columnradius = r*sqrt(2)/n/2.0;
		columnradius = r*sqrt(2)/((n-1)*2+sqrt(2));

		pR45(p);
		p.y += columnradius;
		p.x -= sqrt(2)/2*r;
		p.x += -columnradius*sqrt(2)/2;

		if (mod(n,2) == 1) {
			p.y += columnradius;
		}
		p.y += o;
		pMod1(p.y,columnradius*2);

		float result = -length(p) + columnradius;
		result = max(result, p.x);
		result = min(result, a);
		return -min(result, b);
	} else {
		return -m;
	}
}

float fOpIntersectionColumns(float a, float b, float r, float n, float o) {
	return fOpDifferenceColumns(a,-b,r, n, o);
}

float sdOctahedron( vec3 p, float s)
{
	p = abs(p);
	float m = p.x+p.y+p.z-s;
	vec3 q;
			 if( 3.0*p.x < m ) q = p.xyz;
	else if( 3.0*p.y < m ) q = p.yzx;
	else if( 3.0*p.z < m ) q = p.zxy;
	else return m*0.57735027;

	float k = clamp(0.5*(q.z-q.y+s),0.0,s);
	return length(vec3(q.x,q.y-s+k,q.z-k));
}

float sdOctahedronBound( vec3 p, float s)
{
	p = abs(p);
	return (p.x+p.y+p.z-s)*0.57735027;
}

float sdCappedTorus(in vec3 p, in vec2 sc, in float ra, in float rb)
{
	p.x = abs(p.x);
	float k = (sc.y*p.x>sc.x*p.y) ? dot(p.xy, sc) : length(p.xy);
	return sqrt(dot(p, p) + ra*ra - 2.0*ra*k) - rb;
}

float fCone(vec3 p, float radius, float height, vec3 direction, float offset) {
	p -= direction * offset;
	p = reflect(p, normalize(mix(vec3(0,1,0), -direction, .5)));
	//p -= vec3(0,height,0);
	return fCone(p, radius, height);
}

float sdCappedCone(vec3 p, float h, float r1, float r2)
{
	vec2 q = vec2( length(p.xz), p.y );
	vec2 k1 = vec2(r2,h);
	vec2 k2 = vec2(r2-r1,2.0*h);
	vec2 ca = vec2(q.x-min(q.x,(q.y<0.0)?r1:r2), abs(q.y)-h);
	vec2 cb = q - k1 + k2*clamp( dot(k1-q,k2)/dot2(k2), 0.0, 1.0 );
	float s = (cb.x<0.0 && ca.y<0.0) ? -1.0 : 1.0;
	return s*sqrt( min(dot2(ca),dot2(cb)) );
}

float sdRoundedBox( in vec2 p, in vec2 b, in vec4 r )
{
	r.xy = (p.x>0.0)?r.xy : r.zw;
	r.x  = (p.y>0.0)?r.x  : r.y;
	vec2 q = abs(p)-b+r.x;
	return min(max(q.x,q.y),0.0) + length(max(q,0.0)) - r.x;
}
