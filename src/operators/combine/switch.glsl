ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if THIS_INPUT_COUNT == 0
	initDefVal(res);
	#else
		#ifdef THIS_HAS_INPUT_indexField
		int source = int(inputOp_indexField(p, ctx));
		#else
		int source = int(THIS_Source);
		#endif
		int i = clamp(source, 0, THIS_INPUT_COUNT - 1);
		if (i == 0) {
			res = THIS_INPUT_1(p, ctx);
		}
		#if THIS_INPUT_COUNT > 1
		else if (i == 1) {
			res = THIS_INPUT_2(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 2
		else if (i == 2) {
			res = THIS_INPUT_3(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 3
		else if (i == 3) {
			res = THIS_INPUT_4(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 4
		else if (i == 4) {
			res = THIS_INPUT_5(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 5
		else if (i == 5) {
			res = THIS_INPUT_6(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 6
		else if (i == 6) {
			res = THIS_INPUT_7(p, ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 7
		else if (i == 7) {
			res = THIS_INPUT_8(p, ctx);
		}
		#endif
		else {
			initDefVal(res);
		}
	#endif
	return res;
}