ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#if defined(THIS_RETURN_TYPE_Sdf)
	{
		#ifdef THIS_Enablesmoothing
		res.x = quantize(res.x, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
		#else
		res.x = quantizeHard(res.x, THIS_Size.x, THIS_Offset.x);
		#endif
	}
	#elif defined(THIS_RETURN_TYPE_float)
	{
		#ifdef THIS_Enablesmoothing
		res = quantize(res, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
		#else
		res = quantizeHard(res, THIS_Size.x, THIS_Offset.x);
		#endif
	}
	#else
	{
		#ifdef THIS_Enablesmoothing
		res = quantize(res, THIS_Size, THIS_Offset, THIS_Smoothing);
		#else
		res = quantizeHard(res, THIS_Size, THIS_Offset);
		#endif
	}
	#endif
	return res;
}