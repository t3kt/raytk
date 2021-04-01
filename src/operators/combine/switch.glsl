ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		#ifdef THIS_RETURN_TYPE_Sdf
			return createSdf(0);
		#else
			return ReturnT(0);
		#endif
	#else
		int i = clamp(int(THIS_Source), 0, THIS_INPUT_COUNT - 1);
		if (i == 0) {
			return THIS_INPUT_1(p, ctx);
		}
		#if THIS_INPUT_COUNT > 1
		if (i == 1) {
			return THIS_INPUT_2(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 2
		if (i == 2) {
			return THIS_INPUT_3(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 3
		if (i == 3) {
			return THIS_INPUT_4(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 4
		if (i == 4) {
			return THIS_INPUT_5(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 5
		if (i == 5) {
			return THIS_INPUT_6(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 6
		if (i == 6) {
			return THIS_INPUT_7(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 7
		if (i == 7) {
			return THIS_INPUT_8(p, ctx);
		}
		#endif
		ReturnT val;
		initDefVal(val);
		return val;
	#endif
}