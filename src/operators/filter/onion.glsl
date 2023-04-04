ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		float val = adaptAsFloat(res);
		#ifdef THIS_HAS_INPUT_thicknessField
		float th = inputOp_thicknessField(p, ctx);
		#else
		float th = THIS_Thickness;
		#endif
		#ifdef THIS_HAS_INPUT_iterationsField
		int n = int(inputOp_iterationsField(p, ctx));
		#else
		int n = int(THIS_Iterations);
		#endif
		for (int i = 0; i < n; i++) {
			val = abs(val) - th / float(i + 1);
		}
		setFromFloat(res, val);
	}
	return res;
}