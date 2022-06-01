ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (THIS_Enable >= 0.5 && !isDistanceOnlyStage()) {
		#ifdef THIS_EXPOSE_sdf
		THIS_sdf = res;
		#endif
		#pragma r:if THIS_HAS_INPUT_colorField
		assignColor(res, inputOp_colorField(p, ctx).rgb);
		#pragma r:else
		assignColor(res, THIS_Color);
		#pragma r:endif
	}
	return res;
}