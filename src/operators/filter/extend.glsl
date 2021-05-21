ReturnT thismap(CoordT p, ContextT ctx) {
	p = clamp(p, THIS_asCoordT(THIS_Center - THIS_Size * 0.5), THIS_asCoordT(THIS_Center + THIS_Size * 0.5));
	return inputOp1(p, ctx);
}