ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q0;
	#ifdef THIS_HAS_INPUT_coordField
	q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q0 = adaptAsVec3(p);
	#endif
	int axis = int(THIS_Axis);
	float q;
	if (axis == 3) {
		q = length(q0);
	} else {
		q = getAxis(q0, axis);
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
				return vec4(0);
			}
			break;
	}
	return mix(vec4(THIS_Color1, THIS_Alpha1), vec4(THIS_Color2, THIS_Alpha2), q);
}