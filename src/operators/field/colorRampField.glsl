vec4 thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	float q = inputOp1(p, ctx);
	#else
	float q = p;
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
	return mix(THIS_Color1, THIS_Color2, q);
}