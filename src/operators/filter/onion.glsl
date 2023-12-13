ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		float val = adaptAsFloat(res);
		float val0 = val;
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
		SIDE_BODY();
		#if defined(THIS_RETURN_TYPE_Sdf)
		res.x = val;
		#elif defined(THIS_RETURN_TYPE_float)
		res = val;
		#endif
	}
	return res;
}