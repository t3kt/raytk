ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Instancecount);
	setIterationIndex(ctx, 0);
	ReturnT res1 = inputOp1(p, ctx);
	float r = THIS_Radius;
	for (int i = 0; i < n; i++) {
		setIterationIndex(ctx, i);
		ReturnT res2 = inputOp1(p, ctx);
		#ifdef THIS_COMBINE_EXPR_IS_SDF
		res1 = THIS_COMBINE_EXPR;
		#else
		float h = smoothBlendRatio(res1.x, res2.x, r);
		res1.x = THIS_COMBINE_EXPR;
		blendInSdf(res1, res2, 1.0 - h);
		#endif
	}
	return res1;
}
