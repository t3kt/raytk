ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_RADIUS
		float r = THIS_Radius;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
	#endif
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	if (THIS_Swapinputs > 0.) {
		swap(res1, res2);
	}
	#ifdef THIS_HAS_NUMBER
		float n = THIS_Number;
	#endif
	#ifdef THIS_HAS_OFFSET
		float o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		o *= inputOp_offsetField(p, ctx);
		#endif
	#endif
	float h = smoothBlendRatio(res1.x, res2.x, r);
	BODY();
	return res1;
}