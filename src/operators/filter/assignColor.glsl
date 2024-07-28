ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable) && !isDistanceOnlyStage()) {
		bool use = true;
		CONDITION();
		if (!use) return res;
		#ifdef THIS_EXPOSE_sdf
		#ifdef THIS_RETURN_TYPE_Volume
		THIS_sdf = res.sdf;
		#else
		THIS_sdf = res;
		#endif
		#endif
		#ifdef THIS_HAS_INPUT_colorField
		assignColor(res, fillToVec3(inputOp_colorField(p, ctx)));
		#else
		assignColor(res, THIS_Color);
		#endif
	}
	return res;
}