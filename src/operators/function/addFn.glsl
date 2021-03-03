ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		return THIS_Add;
	#elif THIS_INPUT_COUNT == 1
		return THIS_Add + THIS_INPUT_1(p, ctx);
	#elif THIS_INPUT_COUNT == 2
		return THIS_Add + THIS_INPUT_1(p, ctx) + THIS_INPUT_2(p, ctx);
	#elif THIS_INPUT_COUNT == 3
		return THIS_Add + THIS_INPUT_1(p, ctx) + THIS_INPUT_2(p, ctx) + THIS_INPUT_3(p, ctx);
	#elif THIS_INPUT_COUNT == 4
		return THIS_Add + THIS_INPUT_1(p, ctx) + THIS_INPUT_2(p, ctx) + THIS_INPUT_3 + THIS_INPUT_4(p, ctx);
	#endif
}