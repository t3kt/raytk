ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p -= THIS_asCoordT(THIS_Translate);
	CoordT q = p;
	#ifdef THIS_Enablephase
	p += THIS_asCoordT(THIS_Phase1);
	q += THIS_asCoordT(THIS_Phase2);
	#endif
	#ifdef THIS_HAS_INPUT_phase1Field
	p += THIS_asCoordT(fillToVec3(inputOp_phase1Field(p0, ctx)));
	#endif
	#ifdef THIS_HAS_INPUT_phase2Field
	q += THIS_asCoordT(fillToVec3(inputOp_phase2Field(p0, ctx)));
	#endif
	#ifdef THIS_Enableperiod
	CoordT per1 = THIS_asCoordT(THIS_Period1);
	CoordT per2 = THIS_asCoordT(THIS_Period2);
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
	#ifdef THIS_HAS_INPUT_biasField
	float b = adaptAsFloat(inputOp_biasField(p0, ctx));
	#else
	float b = THIS_Bias;
	#endif
	float d = dot(sin(p), cos(c)) - b;
	d = abs(d);
	d /= length(s);
	#ifdef THIS_Enableperiod
	d /= length(per1) * length(per2);
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = adaptAsFloat(inputOp_thicknessField(p0, ctx));
	#else
	float th = THIS_Thickness;
	#endif
	return createSdf(d - th);
}