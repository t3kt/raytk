ReturnT thismap(CoordT p, ContextT ctx) {
	float ratio = ctx.iteration.x;
	if (ratio != 1.0) {
		#if defined(THIS_EXTEND_clamp)
		ratio = clamp(ratio, 0, 1);
		#elif defined(THIS_EXTEND_loop)
		ratio = fract(ratio);
		#endif
	}
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), ratio);
}