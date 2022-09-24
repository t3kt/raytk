ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	if (IS_TRUE(THIS_Enable)) {
		TRANSFORM_CODE();
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	{
		res = inputOp1(p, ctx);
		#ifdef THIS_RETURN_TYPE_Sdf
		res = withAdjustedScale(res, valueAdjust);
		#else
		res = res * valueAdjust;
		#endif
	}
	#else
	{
		res = adaptAsVec4(p);
	}
	#endif
	return res;
}