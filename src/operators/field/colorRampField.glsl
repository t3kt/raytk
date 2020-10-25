vec4 thismap(CoordT p, ContextT ctx) {
	float amt = inputOp1(p, ctx);
	#ifdef THIS_CLAMP_RANGE
	amt = clamp(amt, 0., 1.);
	#endif
	vec4 color1 = THIS_Color1;
	vec4 color2 = THIS_Color2;
	return mapRange(
		vec4(amt), vec4(0.), vec4(1.), color1, color2);
//	return mix(THIS_Color1, THIS_Color2, amt);
}