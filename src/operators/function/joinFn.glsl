ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	initDefVal(res);
	#if THIS_INPUT_COUNT == 0
	#elif THIS_INPUT_COUNT == 1
		res = THIS_INPUT_1(p, ctx);
	#elif defined(THIS_Fitrange)
	{
		float i = p * float(THIS_INPUT_COUNT);
		if (i <= 1.) {
			res = THIS_INPUT_1(i, ctx);
		}
		else if (i <= 2.) {
			res = THIS_INPUT_2(i - 1., ctx);
		}
		#if THIS_INPUT_COUNT > 2
		else if (i <= 3.) {
			return THIS_INPUT_3(i - 2., ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 3
		else {
			res = THIS_INPUT_4(i - 3., ctx);
		}
		#endif
	}
	#else
	{
		float i = floor(p);
		if (i < 1) {
			res = THIS_INPUT_1(fract(p), ctx);
		} else if (i < 2) {
			res = THIS_INPUT_2(fract(p), ctx);
		}
		#if THIS_INPUT_COUNT > 2
		else if (i == 2) {
			res = THIS_INPUT_3(fract(p), ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 3
		else if (i == 3) {
			res = THIS_INPUT_4(fract(p), ctx);
		}
		#endif
		else {
		}
	}
	#endif
	return res;
}