float THIS_adjust = 1.;

void THIS_transform(inout vec4 q, in CoordT p, inout ContextT ctx) {
	float valueAdjust = 1.0;
	#ifdef THIS_Enabletranslate
	vec3 translate = THIS_Translate;
	#ifdef THIS_HAS_INPUT_translateField
	translate += adaptAsVec3(inputOp_translateField(p, ctx));
	#endif
	#endif
	#ifdef THIS_Enablerotate
	vec3 rotate = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_rotateField
	rotate += radians(adaptAsVec3(inputOp_rotateField(p, ctx)));
	#endif
	#endif
	#if defined(THIS_Enablescale) && defined(THIS_Scaletype_uniform)
	float uniformscale = THIS_Uniformscale;
	#ifdef THIS_HAS_INPUT_scaleField
	uniformscale *= adaptAsFloat(inputOp_scaleField(p, ctx));
	#endif
	#elif defined(THIS_Enablescale) && defined(THIS_Scaletype_separate)
	vec3 scale = THIS_Scale;
	#ifdef THIS_HAS_INPUT_scaleField
	scale *= fillToVec3(inputOp_scaleField(p, ctx));
	#endif
	#endif

	TRANSFORM_CODE();
	THIS_adjust = valueAdjust;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	THIS_adjust = 1.;
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	} else {
		#ifdef THIS_HAS_INPUT_1
		res = inputOp1(p, ctx);
		#endif
	}
	#ifdef THIS_HAS_INPUT_1
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, THIS_adjust);
	#endif
	#else
	res = adaptAsVec4(q);
	#endif
	return res;
}