ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
		float radius = THIS_Radius * inputOp3(p, ctx);
	#else
		float radius = THIS_Radius;
	#endif
	ReturnT res1 = THIS_INPUT_1(p, ctx);
	ReturnT res2 = THIS_INPUT_2(p, ctx);
	#ifdef THIS_RETURN_TYPE_float
		return fOpEngrave(res1, res2, radius);
	#else
	float h = smoothBlendRatio(res1.x, res2.x, radius);
	res1.x = fOpEngrave(res1.x, res2.x, radius);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
	#endif
}