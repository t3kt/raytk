ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	return opSmoothUnionM(res1, res2, THIS_GET_AMOUNT());
}