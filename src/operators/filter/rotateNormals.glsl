ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		vec3 n = ctx.normal;
		TRANSFORM_CODE();
		ctx.normal = n;
	}
	return inputOp1(p, ctx);
}