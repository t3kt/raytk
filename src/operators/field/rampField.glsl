ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q0;
	#ifdef THIS_HAS_INPUT_coordField
	q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q0 = adaptAsVec3(p);
	#endif
	float q;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q0.x; break;
		case THISTYPE_Axis_y: q = q0.y; break;
		case THISTYPE_Axis_z: q = q0.z; break;
		case THISTYPE_Axis_dist: q = length(q0); break;
	}
	q = map01(q, THIS_Range.x, THIS_Range.y);
	switch (THIS_Extendmode) {
		case THISTYPE_Extendmode_hold:
			q = clamp(q, 0, 1);
			break;
		case THISTYPE_Extendmode_repeat:
			q = fract(q);
			break;
		case THISTYPE_Extendmode_mirror:
			q = modZigZag(q);
			break;
		case THISTYPE_Extendmode_zero:
			if (q < 0 || q > 1) {
				return THIS_asReturnT(0);
			}
			break;
	}
	vec4 val1 = THIS_Value1;
	vec4 val2 = THIS_Value2;
	return THIS_asReturnT(mix(val1, val2, q));
}