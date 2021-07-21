ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_1
	r *= inputOp1(p, ctx);
	#endif
	return createSdf(THIS_EXPR);
}