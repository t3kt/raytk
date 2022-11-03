vec3 THIS_wave(CoordT p, ContextT ctx, vec3 q) {
	vec3 res;
	WAVE_PREP();
	WAVE_BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 q = adaptAsVec3(p);
		switch (int(THIS_Axis)) {
			case THISTYPE_Axis_x: q = vec3(q.x); break;
			case THISTYPE_Axis_y: q = vec3(q.y); break;
			case THISTYPE_Axis_z: q = vec3(q.z); break;
			case THISTYPE_Axis_dist: q = vec3(length(q)); break;
		}
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