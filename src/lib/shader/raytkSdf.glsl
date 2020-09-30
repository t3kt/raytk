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

Sdf opSmoothUnionM(Sdf d1, Sdf d2, float k) {
	float h = clamp(0.5 + 0.5*(d2.x-d1.x)/k, 0.0, 1.0);
	float resx = mix(d2.x, d1.x, h) - k*h*(1.0-h);
	Sdf res = d1;
	res.x = resx;
	res.material = d2.material;
	res.material2 = d1.material;
	res.interpolant = h;
	res.refract = d1.refract || d2.refract;
	res.reflect = d1.reflect || d2.reflect;
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
