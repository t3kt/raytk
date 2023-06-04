ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_sidesField
	float n = inputOp_sidesField(p, ctx);
	#else
	float n = THIS_Sides;
	#endif
	float d;
	BODY();
	return createSdf(d);
}