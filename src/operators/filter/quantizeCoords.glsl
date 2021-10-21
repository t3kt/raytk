ReturnT thismap(CoordT p, ContextT ctx) {
	return inputOp1(quantize(p,
		THIS_asCoordT(THIS_Size),
		THIS_asCoordT(THIS_Offset),
		THIS_asCoordT(THIS_Smoothing)), ctx);
}