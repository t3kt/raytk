vec3 THIS_wave(vec3 q) {
	vec3 res;
	WAVE_PREP();
	WAVE_BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	CoordT val = THIS_asCoordT(THIS_Offset + THIS_wave(q) * THIS_Amplitude);
	return adaptAsVec4(val);
}