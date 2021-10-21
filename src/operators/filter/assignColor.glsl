ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (!isDistanceOnlyStage()) {
		#ifdef THIS_HAS_INPUT_colorField
		assignColor(res, inputOp_colorField(p, ctx).rgb);
		#else
		assignColor(res, THIS_Color);
		#endif
	}
	return res;
}