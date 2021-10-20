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
	#if defined(THIS_Enablescale) && defined(THIS_HAS_INPUT_scaleField)
	#if defined(THIS_Scaletype_uniform)
	float baseS = uniformscale;
	#else
	vec3 baseS = scale;
	#endif
	#endif
	for (int i = 0; i < n; i++) {
		float ratio = float(i) / float(n - 1);
	#if defined(THIS_Iterationtype_index)
		setIterationIndex(ctx, float(i));
	#elif defined(THIS_Iterationtype_ratio)
		setIterationIndex(ctx, ratio);
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
	#if defined(THIS_Enablescale) && defined(THIS_HAS_INPUT_scaleField)
		{
			#ifdef inputOp_scaleField_COORD_TYPE_float
			inputOp_scaleField_CoordT q0 = ratio;
			#else
			inputOp_scaleField_CoordT q0 = p;
			#endif
			#ifdef THIS_Scaletype_uniform
			uniformscale = baseS * adaptAsFloat(inputOp_scaleField(q0, ctx));
			#else
			scale = baseS * fillToVec3(inputOp_scaleField(q0, ctx));
			#endif
		}
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