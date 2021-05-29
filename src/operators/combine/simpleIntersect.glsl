ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		ReturnT res;
		initDefVal(res);
	#else
		ReturnT res = THIS_INPUT_1(p, ctx);
		#if THIS_INPUT_COUNT > 1
			res = opSimpleIntersect(res, THIS_INPUT_2(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 2
			res = opSimpleIntersect(res, THIS_INPUT_3(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 3
			res = opSimpleIntersect(res, THIS_INPUT_4(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 4
			res = opSimpleIntersect(res, THIS_INPUT_5(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 5
			res = opSimpleIntersect(res, THIS_INPUT_6(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 6
			res = opSimpleIntersect(res, THIS_INPUT_7(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 7
			res = opSimpleIntersect(res, THIS_INPUT_8(p, ctx));
		#endif
	#endif
	return res;
}