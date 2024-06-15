ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	initDefVal(res);
	#ifdef THIS_HAS_INPUT_primary
	res = inputOp_primary(p, ctx);
	#endif
	return res;
}