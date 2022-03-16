ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	ReturnT a = THIS_asReturnT(inputOp1(p, ctx));
	#else
	ReturnT a = THIS_asReturnT(THIS_Value1);
	#endif
	if (THIS_Enable < 0.5) { return a; }
	#ifdef THIS_HAS_INPUT_2
	ReturnT b = THIS_asReturnT(inputOp2(p, ctx));
	#else
	ReturnT b = THIS_asReturnT(THIS_Value2);
	#endif
	return THIS_EXPR;
}