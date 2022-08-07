ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		p = quantize(p,
			THIS_asCoordT(THIS_Size),
			THIS_asCoordT(THIS_Offset),
			THIS_asCoordT(THIS_Smoothing));
	}
	return inputOp1(p, ctx);
}