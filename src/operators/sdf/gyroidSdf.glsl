ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	CoordT q = p;
	#ifdef THIS_USE_PHASE
	p += THIS_Phase1;
	q += THIS_Phase2;
	#endif
	#ifdef THIS_USE_PERIOD
	p /= THIS_Period1;
	q /= THIS_Period2;
	#endif
	p /= THIS_Scale;
	float d = dot(sin(p), cos(q.zxy)) - THIS_Bias;
	d = abs(d);
	d /= length(THIS_Scale);
	#ifdef THIS_USE_PERIOD
	d /= length(THIS_Period1) * length(THIS_Period2);
	#endif
	return createSdf(d - THIS_Thickness);
}