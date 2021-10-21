ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	float d;
	BODY();
	return createSdf(d);
}