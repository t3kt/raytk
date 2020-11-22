ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		#ifdef THIS_RETURN_TYPE_Sdf
			return createSdf(0);
		#else
			return ReturnT(0);
		#endif
	#elif THIS_INPUT_COUNT == 1
		return THIS_INPUT_1(p, ctx);
	#else
		float blend = clamp(THIS_Blend, 0, THIS_INPUT_COUNT-1);
		if (blend == 0) {
			return THIS_INPUT_1(p, ctx);
		}
		#if THIS_INPUT_COUNT > 1
			if (blend == 1.) {
				return THIS_INPUT_2(p, ctx);
			}
		#endif
		#if THIS_INPUT_COUNT > 2
			if (blend == 2.) {
				return THIS_INPUT_3(p, ctx);
			}
		#endif
		#if THIS_INPUT_COUNT > 3
			if (blend == 3.) {
				return THIS_INPUT_4(p, ctx);
			}
		#endif

		int iA = int(blend);
		ReturnT resA;
		ReturnT resB;
		#if THIS_INPUT_COUNT == 2
			resA = THIS_INPUT_1(p, ctx);
			resB = THIS_INPUT_2(p, ctx);
		#else
			if (iA == 0) {
				resA = THIS_INPUT_1(p, ctx);
				resB = THIS_INPUT_2(p, ctx);
			}
			#if THIS_INPUT_COUNT > 2
				else if (iA == 1) {
					resA = THIS_INPUT_2(p, ctx);
					resB = THIS_INPUT_3(p, ctx);
				}
				#if THIS_INPUT_COUNT > 3
					else if (iA == 2) {
						resA = THIS_INPUT_2(p, ctx);
						resB = THIS_INPUT_3(p, ctx);
					}
				#endif
			#endif
		#endif

		float ratio = fract(blend);
		#if defined(THIS_RETURN_TYPE_Sdf)
		resA.x = mix(resA.x, resB.x, ratio);
		blendInSdf(resA, resB, ratio);
		return resA;
		#else
		return mix(resA, resB, ratio);
		#endif
	#endif
}