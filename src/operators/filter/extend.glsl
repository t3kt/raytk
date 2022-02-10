ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sizeField
	CoordT size = THIS_asCoordT(inputOp_sizeField(p, ctx));
	#else
	CoordT size = THIS_asCoordT(THIS_Size);
	#endif
	#ifdef THIS_HAS_INPUT_centerField
	CoordT center = THIS_asCoordT(inputOp_centerField(p, ctx));
	#else
	CoordT center = THIS_asCoordT(THIS_Center);
	#endif
	p = clamp(p, THIS_asCoordT(center - size * 0.5), THIS_asCoordT(center + size * 0.5));
	return inputOp1(p, ctx);
}