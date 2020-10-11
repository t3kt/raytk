ReturnT thismap(CoordT p, ContextT ctx) {
	float ratio = ctx.iteration.x;
	#if defined(THIS_EXTEND_clamp)
	ratio = clamp(ratio, 0, 1);
	#elif defined(THIS_EXTEND_loop)
	if (fract(ratio) != 0) {
		ratio = fract(ratio);
	}
	#endif
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), ratio);
}