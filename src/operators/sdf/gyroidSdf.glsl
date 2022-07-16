ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p -= THIS_asCoordT(THIS_Translate);
	CoordT q = p;
	#pragma r:if THIS_Enablephase
	p += THIS_asCoordT(THIS_Phase1);
	q += THIS_asCoordT(THIS_Phase2);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_phase1Field
	p += THIS_asCoordT(fillToVec3(inputOp_phase1Field(p0, ctx)));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_phase2Field
	q += THIS_asCoordT(fillToVec3(inputOp_phase2Field(p0, ctx)));
	#pragma r:endif
	#pragma r:if THIS_Enableperiod
	CoordT per1 = THIS_asCoordT(THIS_Period1);
	CoordT per2 = THIS_asCoordT(THIS_Period2);
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
	#pragma r:if THIS_HAS_INPUT_biasField
	float b = adaptAsFloat(inputOp_biasField(p0, ctx));
	#pragma r:else
	float b = THIS_Bias;
	#pragma r:endif
	float d = dot(sin(p), cos(c)) - b;
	d = abs(d);
	d /= length(s);
	#pragma r:if THIS_Enableperiod
	d /= length(per1) * length(per2);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_thicknessField
	float th = adaptAsFloat(inputOp_thicknessField(p0, ctx));
	#pragma r:else
	float th = THIS_Thickness;
	#pragma r:endif
	return createSdf(d - th);
}