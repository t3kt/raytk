Ray thismap(vec2 p, CameraContext ctx) {
	Ray ray;
	vec2 size = ctx.resolution;
	vec2 uv = ((-ctx.resolution+ 2.0 * p) / ctx.resolution.y) / size;

	#if defined(THIS_Layout_grid)
		#ifdef THIS_Rescale
		ctx.resolution /= 2.0;
		p = mod(p, ctx.resolution);
		#endif
		if (uv.x > 0.) {
			if (uv.y > 0.) {
				return inputOp2(p, ctx);
			} else {
				return inputOp4(p, ctx);
			}
		} else {
			if (uv.y > 0.) {
				return inputOp1(p, ctx);
			} else {
				return inputOp3(p, ctx);
			}
		}
	#elif defined(THIS_Layout_horz)
		#ifdef THIS_Rescale
			ctx.resolution.x /= 2.0;
			p.x = mod(p.x, ctx.resolution.x);
		#endif
		if (uv.x > 0.) {
			return inputOp2(p, ctx);
		} else {
			return inputOp1(p, ctx);
		}
	#else
		#ifdef THIS_Rescale
			ctx.resolution.y /= 2.0;
			p.y = mod(p.y, ctx.resolution.y);
		#endif
		if (uv.y < 0.) {
			return inputOp2(p, ctx);
		} else {
			return inputOp1(p, ctx);
		}
	#endif
}