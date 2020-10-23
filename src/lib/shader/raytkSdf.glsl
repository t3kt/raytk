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
	res.x = max(-res1.x, res2.x);
	return res;
}

float opSimpleDiff(float res1, float res2) {
	return max(-res1, res2);
}

Sdf opSmoothUnionM(Sdf res1, Sdf res2, float k) {
	float h = clamp(0.5 + 0.5*(res2.x-res1.x)/k, 0.0, 1.0);
	float resx = mix(res2.x, res1.x, h) - k*h*(1.0-h);
	Sdf res = res1;
	res.x = resx;
	res.material = res2.material;
	res.material2 = res1.material;
	res.interpolant = h;
	res.refract = res1.refract || res2.refract;
	res.reflect = res1.reflect || res2.reflect;
	#ifdef RAYTK_OBJECT_ID_IN_SDF
	if (res2.objectId.x != 0.) {
		res.objectId.y = res2.objectId.x;
		res.objectId.z = h;
	}
	#endif
	return res;
}

float opSmoothUnionM(float d1, float d2, float k) {
	float h = clamp(0.5 + 0.5*(d2-d1)/k, 0.0, 1.0);
	return mix(d2, d1, h) - k*h*(1.0-h);
}

float sdBoundingBox( vec3 p, vec3 b, float e )
{
	p = abs(p)-b;
	vec3 q = abs(p+e)-e;
	return min(min(
		length(max(vec3(p.x,q.y,q.z),0.0))+min(max(p.x,max(q.y,q.z)),0.0),
		length(max(vec3(q.x,p.y,q.z),0.0))+min(max(q.x,max(p.y,q.z)),0.0)),
		length(max(vec3(q.x,q.y,p.z),0.0))+min(max(q.x,max(q.y,p.z)),0.0));
}

#ifdef RAYTK_USE_APOLLONIAN
// https://www.shadertoy.com/view/4ds3zn
float sdApollonian(vec3 p, float s, float scale, out vec4 orb) {
	orb = vec4(1000.0);

	for (int i=0; i<8; i++)
	{
		p = -1.0 + 2.0*fract(0.5*p+0.5);

		float r2 = dot(p, p);

		orb = min(orb, vec4(abs(p), r2));

		float k = s/r2;
		p *= k;
		scale *= k;
	}

	return 0.25*abs(p.y)/scale;
}
#endif// RAYTK_USE_APOLLONIAN

#ifdef RAYTK_USE_MANDELBULB
#define __MANDELBULB_V2
float sdMandelbulb(vec3 p, float power, vec2 shiftThetaPhi, out vec4 trap)
{
	float result;
	#ifndef __MANDELBULB_V2
//	if (length(p) > 1.5) return length(p) - 1.2;
	vec3 z = p;
	float dr = 1.0, r = 0.0, theta, phi;
	for (int i = 0; i < 15; i++) {
		r = length(z);
		if (r>1.5) break;
		dr =  pow(r, power-1.0)*power*dr + 1.0;
		theta = acos(z.z/r) * power + shiftThetaPhi.x;
		phi = atan(z.y, z.x) * power;// + shiftThetaPhi.y;
		if (i > 0) {
			phi += shiftThetaPhi.y;
		}
		float sinTheta = sin(theta);
		z = pow(r, power) * vec3(sinTheta*cos(phi), sinTheta*sin(phi), cos(theta)) + p;
	}
	result = 0.5*log(r)*r/dr;
	#else
	p = p.xzy;
	vec3 w = p;
	float m = dot(w, w);

	trap = vec4(abs(w), m);
	float dz = 1.0;
	for (int i=0; i<4; i++)
	{
		#if 0
		float m2 = m*m;
		float m4 = m2*m2;
		dz = 8.0*sqrt(m4*m2*m)*dz + 1.0;

		float x = w.x; float x2 = x*x; float x4 = x2*x2;
		float y = w.y; float y2 = y*y; float y4 = y2*y2;
		float z = w.z; float z2 = z*z; float z4 = z2*z2;

		float k3 = x2 + z2;
		float k2 = inversesqrt(k3*k3*k3*k3*k3*k3*k3);
		float k1 = x4 + y4 + z4 - 6.0*y2*z2 - 6.0*x2*y2 + 2.0*z2*x2;
		float k4 = x2 - y2 + z2;

		w.x = p.x +  64.0*x*y*z*(x2-z2)*k4*(x4-6.0*x2*z2+z4)*k1*k2;
		w.y = p.y + -16.0*y2*k3*k4*k4 + k1*k1;
		w.z = p.z +  -8.0*y*k4*(x4*x4 - 28.0*x4*x2*z2 + 70.0*x4*z4 - 28.0*x2*z2*z4 + z4*z4)*k1*k2;
		#else
		dz = power*pow(sqrt(m), power-1.0)*dz + 1.0;
		//dz = 8.0*pow(m,3.5)*dz + 1.0;

		float r = length(w);
		float theta = (power*acos(w.y/r) + shiftThetaPhi.x);
		float phi = power*atan(w.x, w.z);
		if (i > 0) {
			phi += shiftThetaPhi.y;
		}
		w = p + pow(r, power) * vec3(sin(theta)*sin(phi), cos(theta), sin(theta)*cos(phi));
		#endif

		trap = min(trap, vec4(abs(w), m));

		m = dot(w, w);
		if (m > 256.0)
		break;
	}

	//	resColor = vec4(m, trap.yzw);

	result = 0.25*log(m)*sqrt(m)/dz;
	#endif
	return result;
}

#endif // RAYTK_USE_MANDELBULB

#ifdef RAYTK_USE_MENGER_SPONGE
// Based on Klems code https://www.shadertoy.com/view/XljSWm

// distance to a menger sponge of n = 1
float _mengerCrossDist( in vec3 p, float crossScale, float boxScale ) {
	vec3 absp = abs(p);
	// get the distance to the closest axis
	float maxyz = max(absp.y, absp.z);
	float maxxz = max(absp.x, absp.z);
	float maxxy = max(absp.x, absp.y);
	float cr = crossScale - (step(maxyz, absp.x)*maxyz+step(maxxz, absp.y)*maxxz+step(maxxy, absp.z)*maxxy);
	// cube
	float cu = max(maxxy, absp.z) - boxScale;
	// remove the cross from the cube
	return max(cr, cu);
}

// menger sponge fractal
float sdMengerSponge(in vec3 p, int n, float scale, float crossScale, float boxScale) {
	float dist = 0.0;
	for (int i = 0; i < n; i++) {
		dist = max(dist, _mengerCrossDist(p, crossScale, boxScale)*scale);
		p = fract((p-1.0)*0.5) * 6.0 - 3.0;
		scale /= 3.0;
	}
	return dist;
}
#endif

float sdCrossSmooth(vec3 p, vec3 size, float r)
{
	float da = fBox2(p.xy,size.xy);
	float db = fBox2(p.yz,size.yz);
	float dc = fBox2(p.zx,size.zx);
	return fOpUnionRound(da,fOpUnionRound(db,dc,r), r);
}

float sdCross(vec2 p, vec2 b, float r)
{
	p = abs(p); p = (p.y>p.x) ? p.yx : p.xy;
	vec2  q = p - b;
	float k = max(q.y,q.x);
	vec2  w = (k>0.0) ? q : vec2(b.y-p.x,-k);
	return sign(k)*length(max(w,0.0)) + r;
}

float sdLink( vec3 p, float len, float radius, float thick )
{
	vec3 q = vec3(p.x, max(abs(p.y)-len,0.0), p.z);
	return length(vec2(length(q.xy)-radius,q.z)) - thick;
}

float sdTetrahedron(vec3 p) {
	return (
		max(
			max(-p.x-p.y-p.z, p.x+p.y-p.z),
			max(-p.x+p.y+p.z, p.x-p.y+p.z))
		-1.)/sqrt(3.0);
}

#ifdef RAYTK_USE_SIERPINSKI_TETRAHEDRON

// http://blog.hvidtfeldts.net/index.php/2011/08/distance-estimated-3d-fractals-iii-folding-space/
//float sdSierpinskiTetrahedron(vec3 p, int n, float scale) {
//	vec3 a1 = vec3(1, 1, 1);
//	vec3 a2 = vec3(-1, -1, 1);
//	vec3 a3 = vec3(1, -1, -1);
//	vec3 a4 = vec3(-1, 1, -1);
//	vec3 c;
//	int i = 0;
//	float dist, d;
//	while (i < n) {
//		c = a1;
//		dist = length(p - a1);
//		d = length(p-a2);
//		if (d < dist) {
//			c = a2;
//			dist = d;
//		}
//		d = length(p-a3);
//		if (d < dist) {
//			c = a3;
//			dist = d;
//		}
//		d = length(p-a4);
//		if (d < dist) {
//			c = a4;
//			dist = d;
//		}
//		p = scale * p-c*(scale - 1.0);
//		i++;
//	}
//	return length(p) * pow(scale, float(-i));
//}

//float sdSierpinskiTetrahedron(vec3 p, int n, float scale, out float orbit) {
//	const vec3 n1 = vec3(1, 1, 0);
//	const vec3 n2 = vec3(1, 0, 1);
//	const vec3 n3 = vec3(0, 1, 1);
//	float s = 1.;
//	orbit = 1e20;
//	for (int i=0;i < n;i++) {
//		orbit = min(orbit, dot(p, p));
//		//tetrahedron folding
//		p -= 2.*min(0., dot(p, n1))*n1;
//		p -= 2.*min(0., dot(p, n2))*n2;
//		p -= 2.*min(0., dot(p, n3))*n3;
//
//		//scaling
//		p = p*scale-1.;
//		s /= scale;
//	}
//	//dis & descale
//	return sdTetrahedron(p) * s;
//}

// https://www.shadertoy.com/view/4dl3Wl

// return distance and address
float sdSierpinskiTetrahedron(vec3 p, int n, out float address)
{
const vec3 va = vec3(  0.0,  0.57735,  0.0 );
const vec3 vb = vec3(  0.0, -1.0,  1.15470 );
const vec3 vc = vec3(  1.0, -1.0, -0.57735 );
const vec3 vd = vec3( -1.0, -1.0, -0.57735 );
	float a = 0.0;
	float s = 1.0;
	float r = 1.0;
	float dm;
	vec3 v;
	for (int i=0; i<n; i++)
	{
		float d, t;
		d = dot(p-va, p-va);              v=va; dm=d; t=0.0;
		d = dot(p-vb, p-vb); if (d<dm) { v=vb; dm=d; t=1.0; }
		d = dot(p-vc, p-vc); if (d<dm) { v=vc; dm=d; t=2.0; }
		d = dot(p-vd, p-vd); if (d<dm) { v=vd; dm=d; t=3.0; }
		p = v + 2.0*(p - v); r*= 2.0;
		a = t + 4.0*a; s*= 4.0;
	}

	address = a/s;
	return (sqrt(dm)-1.0)/r;
}

// https://www.shadertoy.com/view/4tt3Ws
//float sdSierpinskiTetrahedron(vec3 p, int iterations)
//{
//	const float scale = 2.0;
//	vec3 a1 = vec3(0.0, 1.0, 0.0);
//	vec3 a2 = vec3(0.0, -0.5, 1.5470);
//	vec3 a3 = vec3(1.0, -0.5, -0.57735);
//	vec3 a4 = vec3(-1.0, -0.5, -0.57735);
//	vec3 c;
//	float dist, d;
//	int i = 0;
//	for (int n=0; n < iterations; n++) {
//		c = a1; dist = length(p-a1);
//		d = length(p-a2); if (d < dist) { c = a2; dist=d; }
//		d = length(p-a3); if (d < dist) { c = a3; dist=d; }
//		d = length(p-a4); if (d < dist) { c = a4; dist=d; }
//		p = scale * p - c * (scale-1.0);
//		i++;
//	}
//
//	return (length(p)-2.0) * pow(scale, float(-i));
//}

// https://www.shadertoy.com/view/4lBfzR
//float sierpinski(in vec3 z, int iterations){
//	float scale = 2.;
//	for (int n = 0; n < iterations; n++) {
//		if (z.x+z.y<0.){ z.xy = -z.yx; }
//		if (z.x+z.z<0.){ z.xz = -z.zx; }
//		if (z.y+z.z<0.){ z.yz = -z.zy; }
////		z = z*2.-1.+0.3*sin(iTime);
////		if (/*bcolor && */n==2)mat+=vec3(0.3)+sin(z.xyz)*vec3(1.0, 0.24, 0.245);
//	}
//
//	return sdTetrahedron(z) * pow(2., -5.);
//}


#endif  // RAYTK_USE_SIERPINSKI_TETRAHEDRON

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

float sdSquarePrism(vec3 p, vec2 h) {
	return fBox(p, h.xxy);
}

float sdSolidAngle(vec3 p, vec2 c, float ra)
{
	// c is the sin/cos of the angle
	vec2 q = vec2( length(p.xz), p.y );
	float l = length(q) - ra;
	float m = length(q - c*clamp(dot(q,c),0.0,ra) );
	return max(l,m*sign(c.y*q.x-c.x*q.y));
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

float sdPyramid( vec3 p, float h)
{
	float m2 = h*h + 0.25;

	p.xz = abs(p.xz);
	p.xz = (p.z>p.x) ? p.zx : p.xz;
	p.xz -= 0.5;

	vec3 q = vec3( p.z, h*p.y - 0.5*p.x, h*p.x + 0.5*p.y);

	float s = max(-q.x,0.0);
	float t = clamp( (q.y-0.5*p.z)/(m2+0.25), 0.0, 1.0 );

	float a = m2*(q.x+s)*(q.x+s) + q.y*q.y;
	float b = m2*(q.x+0.5*t)*(q.x+0.5*t) + (q.y-m2*t)*(q.y-m2*t);

	float d2 = min(q.y,-q.x*m2-q.y*0.5) > 0.0 ? 0.0 : min(a,b);

	return sqrt( (d2+q.z*q.z)/m2 ) * sign(max(q.z,-p.y));
}

float sdMobiusRing(vec3 p, float radius, float thickness, float rounding, float twist, float twistPhase)
{
	vec3 q = vec3(length(p.xz) - radius, 0., p.y);
	float a = atan (p.z, p.x) + twistPhase * PI;
	pR(q.zx, twist * a);
	return 0.5 * (length(max(abs(q.xz) - thickness, 0.)) - rounding);
}

// https://www.shadertoy.com/view/XsGXR1
//float sdMobiusRingStepped(vec3 p, float radius, float thickness, float rounding, float twist, float steps)
//{
//	float d, a, na, aq;
//	vec3 q = vec3(length(p.xz) - radius, 0., p.y);
//	a = atan (p.z, p.x);
//	pR(q.zx, twist * a);
//	d = length(max(abs(q.xz) - thickness, 0.)) - rounding;
//	q = p;
//	na = floor(steps * atan(q.z, - q.x) / (2. * PI));
//	aq = 2. * PI * (na + 0.5) / steps;
//	pR(q.zx, aq);
//	q.x += radius;
//	pR(q.yx, 0.5 * aq);
//	d = max(
//		d,
//		- max(
//				fBox(q, vec3 (1.1, 1.1, 0.18) * thickness)
//				,
//				-fBox2(q.xy, vec2 (0.5, 0.5) * thickness)
//		)
//	);
//	return 0.5 * d;
//}

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
float sdParabola(in vec2 pos, in float k)
{
	pos.x = abs(pos.x);
	float ik = 1.0/k;
	float p = ik*(pos.y - 0.5*ik)/3.0;
	float q = 0.25*ik*ik*pos.x;
	float h = q*q - p*p*p;
	float r = sqrt(abs(h));
	float x = (h>0.0) ?
	pow(q+r, 1.0/3.0) - pow(abs(q-r), 1.0/3.0)*sign(r-q) :
	2.0*cos(atan(r, q)/3.0)*sqrt(p);
	return length(pos-vec2(x, k*x*x)) * sign(pos.x-x);
}

float sdPie( in vec2 p, in vec2 c, in float r )
{
	p.x = abs(p.x);
	float l = length(p) - r;
	float m = length(p-c*clamp(dot(p,c),0.0,r)); // c = sin/cos of the aperture
	return max(l,m*sign(c.y*p.x-c.x*p.y));
}
