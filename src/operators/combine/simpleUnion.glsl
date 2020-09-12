ReturnT thismap(CoordT p, ContextT ctx) {
	return opSimpleUnion(inputOp1(p, ctx), inputOp2(p, ctx));
}