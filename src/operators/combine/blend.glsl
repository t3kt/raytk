ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		#ifdef THIS_RETURN_TYPE_Sdf
			return createSdf(0);
		#else
			return ReturnT(0);
		#endif
	#else
		float blend = clamp(THIS_Blend, 0, THIS_INPUT_COUNT-1);
		if (blend == 0) {
			return THIS_INPUT_1(p, ctx);
		}
		#if THIS_INPUT_COUNT > 1
			if (blend == 1.) {
				return THIS_INPUT_2(p, ctx);
			}
		#endif
		#if THIS_INPUT_COUNT > 2
			if (blend == 2.) {
				return THIS_INPUT_3(p, ctx);
			}
		#endif
		#if THIS_INPUT_COUNT > 3
			if (blend == 3.) {
				return THIS_INPUT_4(p, ctx);
			}
		#endif


		float ratio = fract(blend);
		int iA = int(blend);

		ReturnT resA;
		ReturnT resB;
		#if THIS_INPUT_COUNT > 3
			if (blend == 1.0) {
				return THIS_INPUT_2(p, ctx);
			}
			if (blend < 1.0) {

			}
			ReturnT res4 = THIS_INPUT_4(p, ctx);
		#endif

		ReturnT res1 = THIS_INPUT_1(p, ctx);
		#if THIS_INPUT_COUNT > 1
			ReturnT res2 = THIS_INPUT_2(p, ctx);
		#endif
		#if THIS_INPUT_COUNT > 2
			ReturnT res3 = THIS_INPUT_3(p, ctx);
		#endif
		return res;
	#endif
}