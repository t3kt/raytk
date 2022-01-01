#ifndef RAYTK_SIERPINSKI_TETRAHEDRON
#define RAYTK_SIERPINSKI_TETRAHEDRON

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


	#endif  // RAYTK_SIERPINSKI_TETRAHEDRON

ReturnT thismap(CoordT p, ContextT ctx) {
	float orbit;
//	float d = sdSierpinskiTetrahedron(
//		p - THIS_Translate,
//		int(THIS_Iterations),
//		THIS_Scale,
//		orbit);
	float d = sdSierpinskiTetrahedron(
		p - THIS_Translate,
		int(THIS_Iterations)
		,		orbit
	);
//	float d = sierpinski(p-THIS_Translate, int(THIS_Iterations));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit);
	#endif
	return res;
}