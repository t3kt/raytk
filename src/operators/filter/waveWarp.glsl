vec3 THIS_wave(vec3 q) {
	vec3 amt;
	BODY();
	return amt;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_COORD_TYPE_float
		float q0 = p;
	#pragma r:elif THIS_Axis_dist
		float q0 = length(p);
	#pragma r:else
		float q0 = p.THIS_Axis;
	#pragma r:endif
	vec3 q = (vec3(q0) / THIS_Period) + THIS_Phase;
	vec3 amt;
	BODY();
	amt = (amt * THIS_Amplitude) + THIS_Offset;
	p -= THIS_asCoordT(amt);
	return inputOp1(p, ctx);
}