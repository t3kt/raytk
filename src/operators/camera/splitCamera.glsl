Ray thismap(vec2 p, CameraContext ctx) {
	vec2 size = ctx.resolution;
	vec2 uv = ((-ctx.resolution+ 2.0 * p) / ctx.resolution.y) / size;
	#ifdef THIS_RESCALE
	#ifdef THIS_SPLIT_X
	ctx.resolution.x *= 0.5;
	#endif
	#ifdef THIS_SPLIT_Y
	ctx.resolution.y *= 0.5;
	#endif
	#endif
	#if defined(THIS_LAYOUT_horzsplit)
	#ifdef THIS_RESCALE
	ctx.resolution.x *= 0.5;
	#endif
	if (uv.x <= 0.5) {
		return inputOp1((localUV * vec2(0.5, 1)) * ctx.resolution, ctx);
	} else {
		return inputOp2(((localUV-0.5) * vec2(0.5, 1)) * ctx.resolution, ctx);
	}
	#elif defined(THIS_LAYOUT_vertsplit)
	#ifdef THIS_RESCALE
	ctx.resolution.y *= 0.5;
	#endif
	if (uv.y>= 0.5) {
		return inputOp1(((uv-0.5) * vec2(1, 0.5)) * ctx.resolution, ctx);
	} else {
		return inputOp2((uv * vec2(1, 0.5)) * ctx.resolution, ctx);
	}
	#elif defined(THIS_LAYOUT_quads)
	
	#else
	return inputOp1(
	#endif
}