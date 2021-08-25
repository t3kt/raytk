ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
	ReturnT res = createNonHitSdf();
	#elif THIS_INPUT_COUNT == 1
	ReturnT res = inputOp1(p, ctx);
	#else
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	if (THIS_Swapinputs > 0.) {
		swap(res1, res2);
	}
	#ifdef THIS_HAS_INPUT_3
	float r = inputOp3(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_4
	float d = inputOp4(p, ctx);
	#else
	float d = THIS_Depth;
	#endif
	float h = smoothBlendRatio(res1.x, res2.x, r);
	BODY();
	blendInSdf(res1, res2, 1.0 - h);
	#endif
	return res1;
}