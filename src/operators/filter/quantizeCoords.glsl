ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		p = quantize(p,
			THIS_asCoordT(THIS_Size),
			THIS_asCoordT(THIS_Offset),
			THIS_asCoordT(THIS_Smoothing));
	}
	return inputOp1(p, ctx);
}