vec3 THIS_wave(CoordT p, ContextT ctx, vec3 q) {
	vec3 res;
	WAVE_PREP();
	WAVE_BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		#pragma r:if THIS_COORD_TYPE_float
		float q0 = p;
		#pragma r:elif THIS_Axis_dist
		float q0 = length(p);
		#pragma r:else
		float q0 = p.THIS_Axis;
		#pragma r:endif
		vec3 q = vec3(q0);
		vec3 amt = THIS_wave(p, ctx, q);
		amt = (amt * THIS_Amplitude) + THIS_Offset;
		p -= THIS_asCoordT(amt);
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}