ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return inputOp1(p, ctx); }
	res = inputOp1(p, ctx);
	#ifdef RAYTK_USE_DENSITY
	#ifdef THIS_EXPOSE_sdf
	THIS_sdf = res;
	#endif
	#ifdef THIS_HAS_INPUT_densityField
	float density = inputOp_densityField(p, ctx);
	#else
	float density = THIS_Density;
	#endif
	res.density = density;
	#endif
	return res;
}