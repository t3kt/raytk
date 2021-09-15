ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	int n = int(THIS_Iterations);
	#ifdef RAYTK_ORBIT_IN_SDF
	vec4 orb = vec4(1000);
	#endif
	TRANSFORM_INIT();
	#if defined(THIS_Enablerotate) && defined(THIS_HAS_INPUT_rotateField)
	vec3 baseRot = rotate;
	#endif
	#if defined(THIS_Enabletranslate) && defined(THIS_HAS_INPUT_translateField)
	vec3 baseT = translate;
	#endif
	for (int i = 0; i < n; i++) {
	#if defined(THIS_HAS_INPUT_rotateField) || defined(THIS_HAS_INPUT_translateField)
		float ratio = float(i) / float(n - 1);
	#endif
	#if defined(THIS_Enablerotate) && defined(THIS_HAS_INPUT_rotateField)
		#ifdef inputOp_rotateField_COORD_TYPE_float
		rotate = baseRot + inputOp_rotateField(ratio, ctx).xyz;
		#else
		rotate = baseRot + inputOp_rotateField(p, ctx).xyz;
		#endif
	#endif
	#if defined(THIS_Enabletranslate) && defined(THIS_HAS_INPUT_translateField)
		#ifdef inputOp_translateField_COORD_TYPE_float
		translate = baseT + inputOp_translateField(ratio, ctx).xyz;
		#else
		translate = baseT + inputOp_translateField(p, ctx).xyz;
		#endif
	#endif
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