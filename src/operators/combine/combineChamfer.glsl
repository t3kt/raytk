ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
	float radius = THIS_Radius * inputOp3(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	#ifdef THIS_Swapinputs
	ReturnT res1 = inputOp2(p, ctx);
	ReturnT res2 = inputOp1(p, ctx);
	#else
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	#endif
	#ifdef THIS_RETURN_TYPE_float
	return THIS_FUNC(res1, res2, radius);
	#else
	float h = smoothBlendRatio(res1.x, res2.x, radius);
	res1.x = THIS_FUNC(res1.x, res2.x, radius);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
	#endif
}