ReturnT thismap(CoordT p, ContextT ctx) {
	float i = ctx.iteration.THIS_Iterationpart;
	#if defined(THIS_Extend_clamp)
	i = clamp(i, 0., 1.);
	#elif defined(THIS_Extend_loop)
	i = mod(i, 2.);
	#endif
	if (i < 0.5) {
		return inputOp1(p, ctx);
	} else {
		return inputOp2(p, ctx);
	}
}