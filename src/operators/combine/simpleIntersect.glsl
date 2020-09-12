ReturnT thismap(CoordT p, ContextT ctx) {
	return opSimpleIntersect(inputOp1(p, ctx), inputOp2(p, ctx));
}