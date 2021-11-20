ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	TRANSFORM_CODE();
	ReturnT res = inputOp1(p, ctx);
#pragma r:if THIS_RETURN_TYPE_Sdf
	return withAdjustedScale(res, valueAdjust);
#pragma r:else
	return res * valueAdjust;
#pragma r:endif
}