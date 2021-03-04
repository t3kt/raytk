vec4 thismap(CoordT p, ContextT ctx) {
	float amt = inputOp1(p, ctx);
	#if defined(THIS_Extendmode_hold)
	amt = clamp(amt, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
	amt = fract(amt);
	#elif defined(THIS_Extendmode_mirror)
	amt = modZigZag(amt);
	#elif defined(THIS_Extendmode_zero)
	if (amt < 0 || amt > 1) {
		return vec4(0);
	}
	#endif
	return mix(THIS_Color1, THIS_Color2, amt);
}