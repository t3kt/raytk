ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		#ifdef THIS_HAS_INPUT_lowField
		ReturnT low = THIS_asReturnT(fillToVec4(inputOp_lowField(p, ctx)));
		#else
		ReturnT low = THIS_asReturnT(THIS_Low);
		#endif
		#ifdef THIS_HAS_INPUT_highField
		ReturnT high = THIS_asReturnT(fillToVec4(inputOp_highField(p, ctx)));
		#else
		ReturnT high = THIS_asReturnT(THIS_High);
		#endif
		#ifdef THIS_HAS_INPUT_blendingField
		float b = inputOp_blendingField(p, ctx);
		#else
		float b = THIS_Blending;
		#endif
		BODY();
	}
	return val;
}