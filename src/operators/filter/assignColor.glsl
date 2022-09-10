ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable) && !isDistanceOnlyStage()) {
		#ifdef THIS_EXPOSE_sdf
		THIS_sdf = res;
		#endif
		#pragma r:if THIS_HAS_INPUT_colorField
		assignColor(res, fillToVec3(inputOp_colorField(p, ctx)));
		#pragma r:else
		assignColor(res, THIS_Color);
		#pragma r:endif
	}
	return res;
}