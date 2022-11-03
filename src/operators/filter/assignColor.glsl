ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable) && !isDistanceOnlyStage()) {
		#ifdef THIS_EXPOSE_sdf
		THIS_sdf = res;
		#endif
		#ifdef THIS_HAS_INPUT_colorField
		assignColor(res, fillToVec3(inputOp_colorField(p, ctx)));
		#else
		assignColor(res, THIS_Color);
		#endif
	}
	return res;
}