ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		#ifdef THIS_RETURN_TYPE_Sdf
			return createSdf(0);
		#else
			return ReturnT(0);
		#endif
	#else
		ReturnT res = THIS_INPUT_1(p, ctx);
		#if THIS_INPUT_COUNT > 1
			res = opSimpleUnion(res, THIS_INPUT_2(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 2
			res = opSimpleUnion(res, THIS_INPUT_3(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 3
			res = opSimpleUnion(res, THIS_INPUT_4(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 4
		res = opSimpleUnion(res, THIS_INPUT_5(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 5
		res = opSimpleUnion(res, THIS_INPUT_6(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 6
		res = opSimpleUnion(res, THIS_INPUT_7(p, ctx));
		#endif
		#if THIS_INPUT_COUNT > 7
		res = opSimpleUnion(res, THIS_INPUT_8(p, ctx));
		#endif
		return res;
	#endif
}