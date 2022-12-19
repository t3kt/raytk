ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = p;
	uv = inputOp_pixelMap(uv / ctx.resolution, ctx).xy * ctx.resolution;
	return inputOp_camera(uv, ctx);
}