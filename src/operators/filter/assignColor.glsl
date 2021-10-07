ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (!isDistanceOnlyStage()) {
		#ifdef THIS_HAS_INPUT_colorField
		assignColor(res, vec4(inputOp_colorField(p, ctx).rgb, 1.));
		#else
		assignColor(res, vec4(THIS_Color, 1.));
		#endif
	}
	return res;
}