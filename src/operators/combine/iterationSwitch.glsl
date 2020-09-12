ReturnT thismap(CoordT p, ContextT ctx) {
	float ratio = clamp(ctx.iteration.x, 0, 1);
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), ratio);
}