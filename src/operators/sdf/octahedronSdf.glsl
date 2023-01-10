ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	p -= THIS_Translate;
	float d;
	BODY();
	return createSdf(d);
}