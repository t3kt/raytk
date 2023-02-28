float THIS_adjust = 1.;

void THIS_transform(inout vec4 q, in CoordT p, inout ContextT ctx) {
	float valueAdjust = 1.0;
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