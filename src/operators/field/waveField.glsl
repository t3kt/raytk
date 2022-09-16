ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q0;
	#if defined(THIS_HAS_INPUT_coordField)
		q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
		q0 = adaptAsVec3(p);
	#endif

	#ifdef THIS_Axis_dist
		float q = length(q0);
	#else
		float q = q0.THIS_Axis;
	#endif
	ReturnT res;
	WAVE_PREP();
	#ifdef THIS_HAS_INPUT_waveFunc
	res = inputOp_waveFunc(fract(q), ctx);
	#else
	WAVE_BODY();
	#endif
	return (res * THIS_Amplitude) + THIS_Offset;
}