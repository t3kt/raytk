void THIS_reflect(inout CoordT p0) {
	vec3 p = adaptAsVec3(p0);
	REFLECT_BODY();
	p0 = THIS_asCoordT(p);
}
#ifdef THIS_Enableaccumulate
void THIS_combine(inout Sdf res1, inout Sdf res2, in CoordT p, in ContextT ctx) {
	MERGE_PREP();
	MERGE_BODY();
}
#endif

void THIS_apply(inout CoordT p, inout ContextT ctx, inout float valueAdjust, out vec4 orb, out ReturnT res) {
	int n = int(THIS_Iterations);
	TRANSFORM_INIT();
	#if defined(THIS_Enablerotate) && defined(THIS_HAS_INPUT_rotateField)
	vec3 baseRot = rotate;
	#endif
	#if defined(THIS_Enabletranslate) && defined(THIS_HAS_INPUT_translateField)
	vec3 baseT = translate;
	#endif
	#if defined(THIS_Enablescale) && defined(THIS_HAS_INPUT_scaleField)
	#ifdef THIS_Scaletype_uniform
	float baseS = uniformscale;
	#else
	vec3 baseS = scale;
	#endif
	#endif
	for (int i = 0; i < n; i++) {
		float ratio = float(i) / float(n - 1);
		switch (int(THIS_Iterationtype)) {
			case THISTYPE_Iterationtype_index:
				setIterationIndex(ctx, float(i));
				break;
			case THISTYPE_Iterationtype_ratio:
				setIterationIndex(ctx, ratio);
				break;
		}
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = ratio;
		#endif
		#if defined(THIS_Enablerotate) && defined(THIS_HAS_INPUT_rotateField)
		rotate = baseRot + inputOp_rotateField(p, ctx).xyz;
		#endif
		#if defined(THIS_Enabletranslate) && defined(THIS_HAS_INPUT_translateField)
		translate = baseT + inputOp_translateField(p, ctx).xyz;
		#endif
		#if defined(THIS_Enablescale) && defined(THIS_HAS_INPUT_scaleField)
		{
			#ifdef THIS_Scaletype_uniform
			uniformscale = baseS * adaptAsFloat(inputOp_scaleField(p, ctx));
			#else
			scale = baseS * fillToVec3(inputOp_scaleField(p, ctx));
			#endif
		}
		#endif
		CoordT preReflectP = p;
		THIS_reflect(p);
		orb = min(orb, vec4(adaptAsVec3(abs(preReflectP - p)), length(p)));
		TRANSFORM_CODE();
		CUSTOM_CODE();

		#ifdef THIS_Enableaccumulate
		if (i == 0) {
			res = inputOp1(p, ctx);
		} else {
			Sdf res1 = inputOp1(p, ctx);
			THIS_combine(res, res1, p, ctx);
		}
		#endif
	}
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	vec4 orb = vec4(1000);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx, valueAdjust, orb, res);
	}
	#ifndef THIS_Enableaccumulate
	res = inputOp1(p, ctx);
	#endif
#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orb);
#endif
#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, valueAdjust);
#endif
	return res;
}