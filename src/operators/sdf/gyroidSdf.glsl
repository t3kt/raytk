ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_asCoordT(THIS_Translate);
	CoordT q = p;
	#pragma r:if THIS_Enablephase
	p += THIS_asCoordT(THIS_Phase1);
	q += THIS_asCoordT(THIS_Phase2);
	#pragma r:endif
	CoordT per1 = THIS_asCoordT(THIS_Period1);
	CoordT per2 = THIS_asCoordT(THIS_Period2);
	#pragma r:if THIS_Enableperiod
	p /= per1;
	q /= per2;
	#pragma r:endif
	CoordT s = THIS_asCoordT(THIS_Scale);
	p /= s;
	#pragma r:if THIS_COORD_TYPE_vec2
	CoordT c = q.xy;
	#pragma r:else
	CoordT c = q.zxy;
	#pragma r:endif
	float d = dot(sin(p), cos(c)) - THIS_Bias;
	d = abs(d);
	d /= length(s);
	#pragma r:if THIS_Enableperiod
	d /= length(per1) * length(per2);
	#pragma r:endif
	return createSdf(d - THIS_Thickness);
}