ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (!isDistanceOnlyStage()) {
		#pragma r:if THIS_HAS_INPUT_colorField
		assignColor(res, inputOp_colorField(p, ctx).rgb);
		#pragma r:else
		assignColor(res, THIS_Color);
		#pragma r:endif
	}
	return res;
}