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

float sdTriPrism( vec3 p, vec2 h )
{
	vec3 q = abs(p);
	return max(q.z-h.y,max(q.x*0.866025+p.y*0.5,-p.y)-h.x*0.5);
}

float sdHexPrism( vec3 p, vec2 h )
{
	const vec3 k = vec3(-0.8660254, 0.5, 0.57735);
	p = abs(p);
	p.xy -= 2.0*min(dot(k.xy, p.xy), 0.0)*k.xy;
	vec2 d = vec2(
		length(p.xy-vec2(clamp(p.x,-k.z*h.x,k.z*h.x), h.x))*sign(p.y-h.x),
		p.z-h.y );
	return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

float sdOctogonPrism( in vec3 p, in float r, float h )
{
	const vec3 k = vec3(-0.9238795325,  // sqrt(2+sqrt(2))/2
											0.3826834323,   // sqrt(2-sqrt(2))/2
											0.4142135623 ); // sqrt(2)-1
	// reflections
	p = abs(p);
	p.xy -= 2.0*min(dot(vec2( k.x,k.y),p.xy),0.0)*vec2( k.x,k.y);
	p.xy -= 2.0*min(dot(vec2(-k.x,k.y),p.xy),0.0)*vec2(-k.x,k.y);
	// polygon side
	p.xy -= vec2(clamp(p.x, -k.z*r, k.z*r), r);
	vec2 d = vec2( length(p.xy)*sign(p.y), p.z-h );
	return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

float sdSquarePrism(vec3 p, vec2 h) {
	return fBox(p, h.xxy);
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

float sdRhombus(in vec2 p, in vec2 b)
{
	vec2 q = abs(p);
	float h = clamp((-2.0*ndot(q,b)+ndot(b,b))/dot(b,b),-1.0,1.0);
	float d = length( q - 0.5*b*vec2(1.0-h,1.0+h) );
	return d * sign( q.x*b.y + q.y*b.x - b.x*b.y );
}

float sdEquilateralTriangle( in vec2 p )
{
	const float k = sqrt(3.0);
	p.x = abs(p.x) - 1.0;
	p.y = p.y + 1.0/k;
	if( p.x+k*p.y>0.0 ) p = vec2(p.x-k*p.y,-k*p.x-p.y)/2.0;
	p.x -= clamp( p.x, -2.0, 0.0 );
	return -length(p)*sign(p.y);
}

float sdTriangleIsosceles( in vec2 p, in vec2 q )
{
	p.x = abs(p.x);
	vec2 a = p - q*clamp( dot(p,q)/dot(q,q), 0.0, 1.0 );
	vec2 b = p - q*vec2( clamp( p.x/q.x, 0.0, 1.0 ), 1.0 );
	float s = -sign( q.y );
	vec2 d = min(
		vec2( dot(a,a), s*(p.x*q.y-p.y*q.x) ),
		vec2( dot(b,b), s*(p.y-q.y)  ));
	return -sqrt(d.x)*sign(d.y);
}

float sdTriangle( in vec2 p, in vec2 p0, in vec2 p1, in vec2 p2 )
{
	vec2 e0 = p1-p0, e1 = p2-p1, e2 = p0-p2;
	vec2 v0 = p -p0, v1 = p -p1, v2 = p -p2;
	vec2 pq0 = v0 - e0*clamp( dot(v0,e0)/dot(e0,e0), 0.0, 1.0 );
	vec2 pq1 = v1 - e1*clamp( dot(v1,e1)/dot(e1,e1), 0.0, 1.0 );
	vec2 pq2 = v2 - e2*clamp( dot(v2,e2)/dot(e2,e2), 0.0, 1.0 );
	float s = sign( e0.x*e2.y - e0.y*e2.x );
	vec2 d = min(min(
		vec2(dot(pq0,pq0), s*(v0.x*e0.y-v0.y*e0.x)),
		vec2(dot(pq1,pq1), s*(v1.x*e1.y-v1.y*e1.x))),
		vec2(dot(pq2,pq2), s*(v2.x*e2.y-v2.y*e2.x)));
	return -sqrt(d.x)*sign(d.y);
}

float sdPentagon( in vec2 p, in float r )
{
	const vec3 k = vec3(0.809016994,0.587785252,0.726542528);
	p.x = abs(p.x);
	p -= 2.0*min(dot(vec2(-k.x,k.y),p),0.0)*vec2(-k.x,k.y);
	p -= 2.0*min(dot(vec2( k.x,k.y),p),0.0)*vec2( k.x,k.y);
	p -= vec2(clamp(p.x,-r*k.z,r*k.z),r);
	return length(p)*sign(p.y);
}
float sdHexagon(in vec2 p, in float r)
{
	const vec3 k = vec3(-0.866025404, 0.5, 0.577350269);
	p = abs(p);
	p -= 2.0*min(dot(k.xy, p), 0.0)*k.xy;
	p -= vec2(clamp(p.x, -k.z*r, k.z*r), r);
	return length(p)*sign(p.y);
}
float sdOctogon(in vec2 p, in float r)
{
	const vec3 k = vec3(-0.9238795325, 0.3826834323, 0.4142135623);
	p = abs(p);
	p -= 2.0*min(dot(vec2(k.x, k.y), p), 0.0)*vec2(k.x, k.y);
	p -= 2.0*min(dot(vec2(-k.x, k.y), p), 0.0)*vec2(-k.x, k.y);
	p -= vec2(clamp(p.x, -k.z*r, k.z*r), r);
	return length(p)*sign(p.y);
}
float sdHexagram(in vec2 p, in float r)
{
	const vec4 k = vec4(-0.5, 0.8660254038, 0.5773502692, 1.7320508076);
	p = abs(p);
	p -= 2.0*min(dot(k.xy, p), 0.0)*k.xy;
	p -= 2.0*min(dot(k.yx, p), 0.0)*k.yx;
	p -= vec2(clamp(p.x, r*k.z, r*k.w), r);
	return length(p)*sign(p.y);
}
float sdStar(in vec2 p, in float r, in float n, in float m)
{
	// next 4 lines can be precomputed for a given shape
	float an = PI/n;
	float en = PI/m;  // m is between 2 and n
	vec2  acs = vec2(cos(an),sin(an));
	vec2  ecs = vec2(cos(en),sin(en)); // ecs=vec2(0,1) for regular polygon,

	float bn = mod(atan(p.x,p.y),2.0*an) - an;
	p = length(p)*vec2(cos(bn),abs(sin(bn)));
	p -= r*acs;
	p += ecs*clamp( -dot(p,ecs), 0.0, r*acs.y/ecs.y);
	return length(p)*sign(p.x);
}

float sdPie( in vec2 p, in vec2 c, in float r )
{
	p.x = abs(p.x);
	float l = length(p) - r;
	float m = length(p-c*clamp(dot(p,c),0.0,r)); // c = sin/cos of the aperture
	return max(l,m*sign(c.y*p.x-c.x*p.y));
}

float sdVesica(vec2 p, float r, float d)
{
	p = abs(p);
	float b = sqrt(r*r-d*d);
	return ((p.y-b)*d>p.x*b) ? length(p-vec2(0.0,b)) : length(p-vec2(-d,0.0))-r;
}

float sdSuperQuad(vec2 p, float e) {
	return pow(pow(p.x,e)+pow(p.y,e),1./e);
}

// Repeat only a few times: from indices <start> to <stop> (similar to above, but more flexible)
float pModIntervalMirror1(inout float p, float size, float start, float stop) {
	float halfsize = size*0.5;
	float c = floor((p + halfsize)/size);
	p = mod(p+halfsize, size) - halfsize;
	p *= mod(c, 2.0)*2 - 1;
	if (c > stop) { //yes, this might not be the best thing numerically.
		p += size*(c - stop);
		c = stop;
	}
	if (c <start) {
		p += size*(c - start);
		c = start;
	}
	return c;
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

//Eiffie
vec2 sdHelixCoords(vec3 p, float r1, float m, float dualSpread) {
	float halfm = m*.5,
	b = mod(p.y, PI*m) - PI*halfm,
	a = abs(atan(p.x, p.z) * halfm - b);
	if (a > PI*halfm) a = PI*m - a;

	//optimisation from Shane
	p.xy = vec2(length(p.xz) - r1, a);
	p.x = abs(p.x) - dualSpread;
	return p.xy;
}

float sdHelix(vec3 p, float r1, float r2, float m, float dualSpread) {
	vec2 q = sdHelixCoords(p, r1, m, dualSpread);
	return length(q) - r2;
}

float sdSegment( in vec2 p, in vec2 a, in vec2 b )
{
	vec2 pa = p-a, ba = b-a;
	float h = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 );
	return length( pa - ba*h );
}
