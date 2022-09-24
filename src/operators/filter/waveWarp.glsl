vec3 THIS_wave(CoordT p, ContextT ctx, vec3 q) {
	vec3 res;
	WAVE_PREP();
	WAVE_BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		#if defined(THIS_COORD_TYPE_float)
		float q0 = p;
		#elif defined(THIS_Axis_dist)
		float q0 = length(p);
		#else
		float q0 = p.THIS_Axis;
		#endif
		vec3 q = vec3(q0);
		vec3 amt = THIS_wave(p, ctx, q);
		amt = (amt * THIS_Amplitude * THIS_Amplitudemult) + THIS_Offset;
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