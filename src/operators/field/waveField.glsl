ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_periodField
	float period = THIS_Period * inputOp_periodField(p, ctx);
	#else
	float period = THIS_Period;
	#endif
	#if defined(THIS_HAS_INPUT_coordField)
		float q = inputOp_coordField(p, ctx);
	#elif defined(THIS_COORD_TYPE_float)
		float q = p;
	#elif defined(THIS_Axis_dist)
		float q = length(p);
	#else
		float q = p.THIS_Axis;
	#endif
	#ifdef THIS_HAS_INPUT_phaseField
	float phase = THIS_Phase + inputOP_phaseField(p, ctx);
	#else
	float phase = THIS_Phase;
	#endif
	q = (q / period) + phase;
	ReturnT res;
	BODY();
	return (res * THIS_Amplitude) + THIS_Offset;
}