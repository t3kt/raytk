ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#if defined(THIS_RETURN_TYPE_Sdf)
	res.x = quantize(res.x, THIS_Size1, THIS_Offset1, THIS_Smoothing1);
	return res;
	#elif defined(THIS_RETURN_TYPE_float)
	return quantize(res, THIS_Size1, THIS_Offset1, THIS_Smoothing1);
	#else
	return quantize(res, THIS_Size, THIS_Offset, THIS_Smoothing);
	#endif
}