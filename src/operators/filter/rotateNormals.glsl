ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 n = ctx.normal;
	TRANSFORM_CODE();
	ctx.normal = n;
	return inputOp1(p, ctx);
}