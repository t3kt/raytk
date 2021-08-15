ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_asCoordT(THIS_Translate);
	CoordT q = p;
	#ifdef THIS_Enablephase
	p += THIS_asCoordT(THIS_Phase1);
	q += THIS_asCoordT(THIS_Phase2);
	#endif
	CoordT per1 = THIS_asCoordT(THIS_Period1);
	CoordT per2 = THIS_asCoordT(THIS_Period2);
	#ifdef THIS_Enableperiod
	p /= per1;
	q /= per2;
	#endif
	CoordT s = THIS_asCoordT(THIS_Scale);
	p /= s;
	#ifdef THIS_COORD_TYPE_vec2
	CoordT c = q.xy;
	#else
	CoordT c = q.zxy;
	#endif
	float d = dot(sin(p), cos(c)) - THIS_Bias;
	d = abs(d);
	d /= length(s);
	#ifdef THIS_Enableperiod
	d /= length(per1) * length(per2);
	#endif
	return createSdf(d - THIS_Thickness);
}