ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	#pragma r:if THIS_HAS_INPUT_2
	ReturnT res2 = inputOp2(p, ctx);
	if (THIS_Swapinputs > 0.) {
		swap(res1, res2);
	}
		#pragma r:if THIS_HAS_RADIUS
	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	#pragma r:endif
	#pragma r:if THIS_HAS_NUMBER
		float n = THIS_Number;
	#pragma r:endif
	#pragma r:if THIS_HAS_OFFSET
		float o = THIS_Offset;
		#pragma r:if THIS_HAS_INPUT_offsetField
		o *= inputOp_offsetField(p, ctx);
		#pragma r:endif
	#pragma r:endif
	float h = smoothBlendRatio(res1.x, res2.x, r);
	BODY();
	#pragma r:endif
	return res1;
}