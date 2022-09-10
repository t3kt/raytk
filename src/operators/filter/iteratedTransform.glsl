void THIS_apply(inout CoordT p, inout ContextT ctx, inout float valueAdjust, out vec4 orb) {
	int n = int(THIS_Iterations);
	TRANSFORM_INIT();
	#pragma r:if THIS_Enablerotate && THIS_HAS_INPUT_rotateField
	vec3 baseRot = rotate;
	#pragma r:endif
	#pragma r:if THIS_Enabletranslate && THIS_HAS_INPUT_translateField
	vec3 baseT = translate;
	#pragma r:endif
	#pragma r:if THIS_Enablescale && THIS_HAS_INPUT_scaleField
	#pragma r:if THIS_Scaletype_uniform
	float baseS = uniformscale;
	#pragma r:else
	vec3 baseS = scale;
	#pragma r:endif
	#pragma r:endif
	for (int i = 0; i < n; i++) {
		float ratio = float(i) / float(n - 1);
		#pragma r:if THIS_Iterationtype_index
		setIterationIndex(ctx, float(i));
		#pragma r:elif THIS_Iterationtype_ratio
		setIterationIndex(ctx, ratio);
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_step
		THIS_step = i;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normstep
		THIS_normstep = ratio;
		#pragma r:endif
		#pragma r:if THIS_Enablerotate && THIS_HAS_INPUT_rotateField
		rotate = baseRot + inputOp_rotateField(p, ctx).xyz;
		#pragma r:endif
		#pragma r:if THIS_Enabletranslate && THIS_HAS_INPUT_translateField
		translate = baseT + inputOp_translateField(p, ctx).xyz;
		#pragma r:endif
		#pragma r:if THIS_Enablescale && THIS_HAS_INPUT_scaleField
		{
			#pragma r:if THIS_Scaletype_uniform
			uniformscale = baseS * adaptAsFloat(inputOp_scaleField(p, ctx));
			#pragma r:else
			scale = baseS * fillToVec3(inputOp_scaleField(p, ctx));
			#pragma r:endif
		}
			#pragma r:endif
		CoordT preReflectP = p;
		THIS_REFLECT();
		orb = min(orb, vec4(adaptAsVec3(abs(preReflectP - p)), length(p)));
		TRANSFORM_CODE();
		CUSTOM_CODE();
	}
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	vec4 orb = vec4(1000);
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx, valueAdjust, orb);
	}
	ReturnT res = inputOp1(p, ctx);
#pragma r:if RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orb);
#pragma r:endif
#pragma r:if THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, valueAdjust);
#pragma r:endif
	return res;
}