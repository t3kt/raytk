vec4 thismap(CoordT p, ContextT ctx) {
	float amt = inputOp1(p, ctx);
	#ifdef THIS_CLAMP_RANGE
	amt = clamp(amt, 0., 1.);
	#endif
	return mix(THIS_Color1, THIS_Color2, amt);
}