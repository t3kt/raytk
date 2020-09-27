ReturnT thismap(CoordT p, ContextT ctx) {
	return inputOp1(quantize(p, THIS_Size, THIS_Offset, THIS_Smoothing), ctx);
}