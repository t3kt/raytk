ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		pR(p.yz, -atan(1./sqrt(2.)));
		pR(p.xz, PI/4.0);
	}
	return inputOp1(p, ctx);
}