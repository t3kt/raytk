ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(inputOp2_RETURN_TYPE_Sdf)
	float lim = inputOp2(p, ctx).x;
	#elif defined(inputOp2_RETURN_TYPE_float)
	float lim = inputOp2(p, ctx).x;
	#else
	#error unsupportedInput2Type
	#endif
	if (lim > RAYTK_SURF_DIST) {
		#if defined(THIS_RETURN_TYPE_Sdf)
		return createSdf(RAYTK_SURF_DIST);
		#elif defined(THIS_RETURN_TYPE_float)
		return RAYTK_SURF_DIST;
		#else
		#error unspportedInput1Type
		#endif
	}
	return inputOp1(p, ctx);
}