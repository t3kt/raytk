ReturnT thismap(CoordT p, ContextT ctx) {
	float q;
	vec3 q0;
	#if defined(THIS_HAS_INPUT_coordField)
	q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q0 = adaptAsVec3(p);
	#endif
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q0.x; break;
		case THISTYPE_Axis_y: q = q0.y; break;
		case THISTYPE_Axis_z: q = q0.z; break;
		case THISTYPE_Axis_dist: q = length(q0); break;
	}
	ReturnT res;
	WAVE_PREP();
	#ifdef THIS_HAS_INPUT_waveFunc
	res = inputOp_waveFunc(fract(q), ctx);
	#else
	WAVE_BODY();
	#endif
	float amp = THIS_Amplitude;
	#ifdef THIS_HAS_INPUT_ampField
	amp *= inputOp_ampField(p, ctx);
	#endif
	return (res * amp) + THIS_Offset;
}