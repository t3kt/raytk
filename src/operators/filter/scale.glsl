ReturnT thismap(CoordT p, ContextT ctx) {
	float adjust = 1.;
	if (THIS_Enable >= 0.5) {
		#pragma r:if THIS_Scaletype_uniform
		float scale = THIS_Uniformscale;
		#pragma r:if THIS_HAS_INPUT_scaleField
		scale *= adaptAsFloat(inputOp_scaleField(p, ctx));
		#pragma r:endif
		adjust = scale;
		#pragma r:elif THIS_Scaletype_separate
		CoordT scale = THIS_asCoordT(THIS_Scale);
		#pragma r:if THIS_HAS_INPUT_scaleField
		scale *= THIS_asCoordT(fillToVec3(inputOp_scaleField(p, ctx)));
		#pragma r:endif
		adjust = vmin(scale);
		#pragma r:else
		#error invalidScaleType
		#pragma r:endif
		p /= scale;
	}

	#pragma r:if THIS_HAS_INPUT_1
	ReturnT res = inputOp1(p, ctx);
	#pragma r:if THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, adjust);
	#pragma r:endif
	#pragma r:else
	ReturnT res = adaptAsVec4(p);
	#pragma r:endif
	return res;
}
