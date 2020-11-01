float thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_USE_INPUT
	float q = inputOp1(p, ctx);
	#else
	float q = p.THIS_AXIS;
	#endif
	float val = THIS_FUNC((p / THIS_Period) + THIS_Phase);
	return (val * THIS_Amplitude) + THIS_Offset;
}