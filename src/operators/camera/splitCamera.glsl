Ray thismap(vec2 p, CameraContext ctx) {
	Ray ray;

	#if THIS_INPUT_COUNT == 1
	ray = inputOp1(p, ctx);
	#elif defined(THIS_cameraMap)
  {
		float mapVal = texture(THIS_cameraMap, p / ctx.resolution).r;
		int i = int(round(mapVal * (THIS_INPUT_COUNT - 1)));
		if (i <= 0) {
			ray = inputOp1(p, ctx);
		} else {
			#if THIS_INPUT_COUNT == 2
			ray = inputOp2(p, ctx);
			#else
      {
				if (i <= 1) {
					ray = inputOp2(p, ctx);
				} else {
					#if THIS_INPUT_COUNT == 3
					ray = inputOp3(p, ctx);
					#else
					if (i <= 2) {
						ray = inputOp3(p, ctx);
					} else {
						ray = inputOp4(p, ctx);
					}
					#endif
				}
			}
			#endif
		}
	}
	#else
	vec2 size = ctx.resolution;
	vec2 uv = ((-ctx.resolution+ 2.0 * p) / ctx.resolution.y) / size;
	#if defined(THIS_Layout_grid) && THIS_INPUT_COUNT == 4
		#ifdef THIS_Rescale
		ctx.resolution /= 2.0;
		p = mod(p, ctx.resolution);
		#endif
		if (uv.x > 0.) {
			if (uv.y > 0.) {
				ray = inputOp2(p, ctx);
			} else {
				ray = inputOp4(p, ctx);
			}
		} else {
			if (uv.y > 0.) {
				ray = inputOp1(p, ctx);
			} else {
				ray = inputOp3(p, ctx);
			}
		}
	#elif defined(THIS_Layout_vert)
		#ifdef THIS_Rescale
		ctx.resolution.y /= 2.0;
		p.y = mod(p.y, ctx.resolution.y);
		#endif
		if (uv.y < 0.) {
			ray = inputOp2(p, ctx);
		} else {
			ray = inputOp1(p, ctx);
		}
	#endif
	#else
		#ifdef THIS_Rescale
		ctx.resolution.x /= 2.0;
		p.x = mod(p.x, ctx.resolution.x);
		#endif
		if (uv.x > 0.) {
			ray = inputOp2(p, ctx);
		} else {
			ray = inputOp1(p, ctx);
		}
	#endif
	return ray;
}