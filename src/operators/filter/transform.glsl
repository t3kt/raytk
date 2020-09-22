ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	TRANSFORM_CODE();
	ReturnT res = inputOp1(p, ctx);
#ifdef THIS_RETURN_TYPE_Sdf
	res.x *= valueAdjust;
	return res;
#else
	return res * valueAdjust;
#endif
}