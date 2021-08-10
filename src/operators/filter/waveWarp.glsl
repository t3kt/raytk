ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_float)
		float q = p;
	#elif defined(THIS_Axis_dist)
		float q = length(p);
	#else
		float q = p.THIS_Axis;
	#endif
	q = (q / THIS_Period) + THIS_Phase;
	float amt;
	BODY();
	amt = (amt * THIS_Amplitude) + THIS_Offset;
	p -= THIS_asCoordT(THIS_Amount) * amt;
	return inputOp1(p, ctx);
}