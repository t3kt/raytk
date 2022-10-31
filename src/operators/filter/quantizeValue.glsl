ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		#if defined(THIS_RETURN_TYPE_Sdf)
		{
			if (IS_TRUE(THIS_Enablesmoothing)) {
				res.x = quantize(res.x, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
			} else {
				res.x = quantizeHard(res.x, THIS_Size.x, THIS_Offset.x);
			}
		}
		#elif defined(THIS_RETURN_TYPE_float)
		{
			if (IS_TRUE(THIS_Enablesmoothing)) {
				res = quantize(res, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
			} else {
				res = quantizeHard(res, THIS_Size.x, THIS_Offset.x);
			}
		}
		#else
		{
			if (IS_TRUE(THIS_Enablesmoothing)) {
				res = quantize(res, THIS_Size, THIS_Offset, THIS_Smoothing);
			} else {
				res = quantizeHard(res, THIS_Size, THIS_Offset);
			}
		}
		#endif
	}
	return res;
}