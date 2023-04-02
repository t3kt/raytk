void THIS_exposeIndex(int i) {
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray;

	THIS_exposeIndex(0);
	#if THIS_INPUT_COUNT == 1
	ray = inputOp1(p, ctx);
	#elif defined(THIS_cameraMap)
  {
		float mapVal = texture(THIS_cameraMap, p / ctx.resolution).r;
		int i = int(round(mapVal * (THIS_INPUT_COUNT - 1)));
		i = clamp(i, 0, THIS_INPUT_COUNT - 1);
		if (i <= 0) {
			THIS_exposeIndex(0);
			ray = THIS_INPUT_1(p, ctx);
		} else {
			#if THIS_INPUT_COUNT == 2
			THIS_exposeIndex(1);
			ray = inputOp2(p, ctx);
			#else
      {
				if (i <= 1) {
					THIS_exposeIndex(1);
					ray = THIS_INPUT_2(p, ctx);
				} else {
					#if THIS_INPUT_COUNT == 3
					THIS_exposeIndex(2);
					ray = THIS_INPUT_3(p, ctx);
					#else
					if (i <= 2) {
						THIS_exposeIndex(2);
						ray = THIS_INPUT_3(p, ctx);
					} else {
						THIS_exposeIndex(3);
						ray = THIS_INPUT_4(p, ctx);
					}
					#endif
				}
			}
			#endif
		}
	}
	#else
	{
		vec2 size = ctx.resolution;
		vec2 uv = ((-ctx.resolution+ 2.0 * p) / ctx.resolution.y) / size;
		#if defined(THIS_Layout_grid) && THIS_INPUT_COUNT == 4
		{
			#ifdef THIS_Rescale
			ctx.resolution /= 2.0;
			p = mod(p, ctx.resolution);
			#endif
			if (uv.x > 0.) {
				if (uv.y > 0.) {
					THIS_exposeIndex(1);
					ray = THIS_INPUT_2(p, ctx);
				} else {
					THIS_exposeIndex(3);
					ray = THIS_INPUT_4(p, ctx);
				}
			} else {
				if (uv.y > 0.) {
					THIS_exposeIndex(0);
					ray = THIS_INPUT_1(p, ctx);
				} else {
					THIS_exposeIndex(2);
					ray = THIS_INPUT_3(p, ctx);
				}
			}
		}
		#else
		{
			float j;
			#if defined(THIS_Layout_vert)
			{
				j = p.y / ctx.resolution.y;
				#ifdef THIS_Rescale
				ctx.resolution.y /= THIS_INPUT_COUNT;
				p.y = mod(p.y, ctx.resolution.y);
				#endif
			}
			#elif defined(THIS_Layout_horz) || (defined(THIS_Layout_grid) && THIS_INPUT_COUNT < 4)
			{
				j = p.x / ctx.resolution.x;
				#ifdef THIS_Rescale
				ctx.resolution.x /= THIS_INPUT_COUNT;
				p.x = mod(p.x, ctx.resolution.x);
				#endif
			}
			#else
			#error invalidLayout
			#endif

			int i = int(j * THIS_INPUT_COUNT);
			if (i == 0) {
				THIS_exposeIndex(0);
				ray = THIS_INPUT_1(p, ctx);
			}
			#if THIS_INPUT_COUNT > 1
			else if (i == 1) {
				THIS_exposeIndex(1);
				ray = THIS_INPUT_2(p, ctx);
			}
			#endif
			#if THIS_INPUT_COUNT > 2
			else if (i == 2) {
				THIS_exposeIndex(2);
				ray = THIS_INPUT_3(p, ctx);
			}
			#endif
			#if THIS_INPUT_COUNT > 3
			else if (i == 3) {
				THIS_exposeIndex(3);
				ray = THIS_INPUT_4(p, ctx);
			}
			#endif
			else {
				initDefVal(ray);
			}
		}
		#endif
	}
	#endif
	return ray;
}