#define __MANDELBULB_V2
ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 orb;
	p -= THIS_Translate;
	float power = THIS_Power;
	vec2 shiftThetaPhi = vec2(THIS_Thetashift, THIS_Phishift);
	float thetaShift = THIS_Thetashift;
	float phiShift = THIS_Phishift;

	int n = THIS_Iterations;
	float d;
	#ifndef __MANDELBULB_V2
	n *= 3;
//	if (length(p) > 1.5) return length(p) - 1.2;
	vec3 z = p;
	float dr = 1.0, r = 0.0, theta, phi;
	for (int i = 0; i < n; i++) {
		r = length(z);
		if (r>1.5) break;
		dr =  pow(r, power-1.0)*power*dr + 1.0;
		theta = acos(z.z/r) * power + thetaShift;
		phi = atan(z.y, z.x) * power;// + phiShift;
		if (i > 0) {
			phi += phiShift;
		}
		float sinTheta = sin(theta);
		z = pow(r, power) * vec3(sinTheta*cos(phi), sinTheta*sin(phi), cos(theta)) + p;
	}
	d = 0.5*log(r)*r/dr;
	#else
	p = p.xzy;
	vec3 w = p;
	float m = dot(w, w);

	orb = vec4(abs(w), m);
	float dz = 1.0;
	for (int i=0; i<n; i++)
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
		float theta = (power*acos(w.y/r) + thetaShift);
		float phi = power*atan(w.x, w.z);
		if (i > 0) {
			phi += phiShift;
		}
		w = p + pow(r, power) * vec3(sin(theta)*sin(phi), cos(theta), sin(theta)*cos(phi));
		#endif

		orb = min(orb, vec4(abs(w), m));

		m = dot(w, w);
		if (m > 256.0)
		break;
	}

	//	resColor = vec4(m, orb.yzw);

	d = 0.25*log(m)*sqrt(m)/dz;
	#endif
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}