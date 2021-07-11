ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_HAS_INPUT_2
	res.color = vec4(inputOp2(p, ctx).rgb, 1.);
	#else
	res.color = vec4(THIS_Color, 1.);
	#endif
	return res;
}