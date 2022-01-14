vec3 THIS_wave(vec3 q) {
	vec3 res;
	WAVE_PREP();
	WAVE_BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#pragma r:else
	vec3 q = adaptAsVec3(p);
	#pragma r:endif
	CoordT val = THIS_asCoordT(THIS_Offset + THIS_wave(q) * THIS_Amplitude);
	return adaptAsVec4(val);
}