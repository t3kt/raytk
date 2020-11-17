ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	int n = int(THIS_Iterations);
	#ifdef RAYTK_ORBIT_IN_SDF
	vec4 orb = vec4(1000);
	#endif
	for (int i = 0; i < n; i++) {
	#ifdef RAYTK_ORBIT_IN_SDF
		CoordT q = p;
	#endif
		THIS_REFLECT();
	#ifdef RAYTK_ORBIT_IN_SDF
		orb = min(orb, vec4(abs(q - p), length(p)));
	#endif
		TRANSFORM_CODE();
		CUSTOM_CODE();
	}
	ReturnT res = inputOp1(p, ctx);
#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orb);
#endif
#ifdef THIS_RETURN_TYPE_Sdf
	res.x *= valueAdjust;
	return res;
#else
	return res * valueAdjust;
#endif
}