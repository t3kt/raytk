ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	initDefVal(res);
#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
#endif
	return res;
}