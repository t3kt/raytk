ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = p;
	if (IS_TRUE(THIS_Enable)) {
		uv = inputOp_pixelMap(uv / ctx.resolution, ctx).xy * ctx.resolution;
	}
	return inputOp_camera(uv, ctx);
}