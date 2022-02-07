ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 orb;
	p -= THIS_Translate;
	float power = THIS_Power;
	vec2 shift0 = vec2(THIS_Thetashift, THIS_Phishift);
	vec2 shift = shift0;

	int n = THIS_Iterations;
	float d;
	p = p.xzy;
	vec3 w = p;
	float m = dot(w, w);

	orb = vec4(abs(w), m);
	float dz = 1.0;
	for (int i=0; i<n; i++)
	{
		dz = power*pow(sqrt(m), power-1.0)*dz + 1.0;
		//dz = 8.0*pow(m,3.5)*dz + 1.0;

		float r = length(w);

		#pragma r:if THIS_EXPOSE_step
		THIS_step = i;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#pragma r:endif

		#ifdef THIS_HAS_INPUT_shiftField
		shift = shift0 + radians(adaptAsVec2(inputOp_shiftField(p, ctx)));
		#endif

		float theta = (power*acos(w.y/r) + shift.x);
		float phi = power*atan(w.x, w.z);
		if (i > 0) {
			phi += shift.y;
		}
		w = p + pow(r, power) * vec3(sin(theta)*sin(phi), cos(theta), sin(theta)*cos(phi));

		orb = min(orb, vec4(abs(w), m));

		m = dot(w, w);
		if (m > 256.0) break;
	}

	d = 0.25*log(m)*sqrt(m)/dz;
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}