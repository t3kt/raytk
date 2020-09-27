ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res.x = quantize(res.x, THIS_Size1, THIS_Offset1, THIS_Smoothing1);
	return res;
	#else
	return quantize(res, THIS_Size, THIS_Offset, THIS_Smoothing);
	#endif
}