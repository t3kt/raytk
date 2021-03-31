ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_1)
	return inputOp1(p, ctx);
	#else
	ReturnT val;
	initDefVal(val);
	return val;
	#endif
}
