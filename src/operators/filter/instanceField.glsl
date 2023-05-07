void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	setIterationIndex(ctx, i);
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
	#ifdef THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = ReturnT(0.);
	if (IS_FALSE(THIS_Enable)) {
		THIS_exposeIndex(ctx, 0, 1);
		res = inputOp1(p, ctx);
	} else {
		int n = int(THIS_Instancecount);
		THIS_exposeIndex(ctx, 0, n);
		res = inputOp1(p, ctx);
		for (int i = 1; i < n; i++) {
			THIS_exposeIndex(ctx, i, n);
			ReturnT a = res;
			ReturnT b = inputOp1(p, ctx);
			COMBINE_BODY();
		}
	}
	return res;
}