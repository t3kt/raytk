ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	float q = inputOp_coordField(p, ctx);
	#elif defined(THIS_Axis_dist)
	float q = length(p);
	#else
	float q = p.THIS_Axis;
	#endif
	#if defined(THIS_Extendmode_hold)
	q = clamp(q, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
	q = fract(q);
	#elif defined(THIS_Extendmode_mirror)
	q = modZigZag(q);
	#elif defined(THIS_Extendmode_zero)
	if (q < 0 || q > 1) {
		return vec4(0);
	}
	#endif
	return mix(vec4(THIS_Color1, THIS_Alpha1), vec4(THIS_Color2, THIS_Alpha2), q);
}