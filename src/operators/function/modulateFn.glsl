ReturnT thismap(CoordT p, ContextT ctx) {
	return inputOp1(inputOp1_asCoordT(inputOp2(p, ctx)) + p, ctx);
}