ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_GET_RADIUS
	float r = THIS_GET_RADIUS();
	#endif
	ReturnT res1 = THIS_INPUT_1(p, ctx);
	ReturnT res2 = THIS_INPUT_2(p, ctx);
	#ifdef THIS_GET_RADIUS
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = THIS_EXPR;
	blendInSdf(res1, res2, h);
	#else
	res1.x = THIS_EXPR;
	#endif
	return res1;
}