ReturnT thismap(CoordT p, ContextT ctx) {
	float x = p;
	#ifdef THIS_HAS_INPUT_phaseField
	float c = inputOp_phaseField(p, ctx);
	#else
	float c = THIS_Phase;
	#endif
	#ifdef THIS_HAS_INPUT_widthField
	float w = inputOp_widthField(p, ctx);
	#else
	float w = THIS_Width;
	#endif
	x = abs(x - c);
	if (x>w) return 0.0;
	x /= w;
	return 1.0 - x*x*(3.0-2.0*x);
}