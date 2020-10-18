ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_INPUT_2_RETURN_Sdf)
	float lim = inputOp2(p, ctx).x;
	#elif defined(THIS_INPUT_2_RETURN_float)
	float lim = inputOp2(p, ctx).x;
	#else
	#error unsupported input 2 type
	#endif
	if (lim < RAYTK_SURF_DIST) {
		#if defined(THIS_INPUT_1_RETURN_Sdf)
		return createSdf(RAYTK_SURF_DIST);
		#elif defined(THIS_INPUT_1_RETURN_float)
		return RAYTK_SURF_DIST;
		#else
		#error unspported input 1 type
		#endif
	}
	return inputOp1(p, ctx);
}