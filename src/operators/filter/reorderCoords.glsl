ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		p = p.THIS_SWIZZLE;
	}
	return inputOp1(p, ctx);
}
