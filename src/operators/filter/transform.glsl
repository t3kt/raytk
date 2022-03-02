ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	if (THIS_Enable >= 0.5) {
		TRANSFORM_CODE();
	}
	ReturnT res;
	#pragma r:if THIS_HAS_INPUT_1
	{
		res = inputOp1(p, ctx);
		#pragma r:if THIS_RETURN_TYPE_Sdf
		res = withAdjustedScale(res, valueAdjust);
		#pragma r:else
		res = res * valueAdjust;
		#pragma r:endif
	}
	#pragma r:else
	{
		res = adaptAsVec4(p);
	}
	#pragma r:endif
	return res;
}