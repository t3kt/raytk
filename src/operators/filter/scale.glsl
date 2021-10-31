ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Scaletype_uniform
	float scale = THIS_Uniformscale;
	#pragma r:if THIS_HAS_INPUT_scaleField
	scale *= adaptAsFloat(inputOp_scaleField(p, ctx));
	#pragma r:endif
	float adjust = scale;
	#pragma r:elif THIS_Scaletype_separate
	CoordT scale = THIS_asCoordT(THIS_Scale);
	#pragma r:if THIS_HAS_INPUT_scaleField
	scale *= THIS_asCoordT(fillToVec3(inputOp_scaleField(p, ctx)));
	#pragma r:endif
	float adjust = vmin(scale);
	#pragma r:else
	#error invalidScaleType
	#pragma r:endif

	ReturnT res = inputOp1(p / scale, ctx);
	#pragma r:if THIS_RETURN_TYPE_float
	res *= adjust;
	#pragma r:else
	res.x *= adjust;
	#pragma r:endif
	return res;
}
