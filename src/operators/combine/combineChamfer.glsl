ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
	float r = THIS_Radius * inputOp3(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	if (THIS_Swapinputs > 0.) {
		swap(res1, res2);
	}
	float h = smoothBlendRatio(res1.x, res2.x, r);
	BODY();
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}