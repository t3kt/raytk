ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	float r = THIS_Amount;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	return opSmoothUnionM(res1, res2, r);
}