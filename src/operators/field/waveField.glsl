ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_2
	float period = THIS_Period * inputOp2(p, ctx);
	#else
	float period = THIS_Period;
	#endif
	#if defined(THIS_HAS_INPUT_1)
		float q = inputOp1(p, ctx);
	#elif defined(THIS_COORD_TYPE_float)
		float q = p;
	#elif defined(THIS_Axis_dist)
		float q = length(p);
	#else
		float q = p.THIS_Axis;
	#endif
	q = (q / period) + THIS_Phase;
	ReturnT res = THIS_FUNC(q);
	return (res * THIS_Amplitude) + THIS_Offset;
}