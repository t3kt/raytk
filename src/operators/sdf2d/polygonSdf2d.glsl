ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	float d;
	BODY();
	return createSdf(d);
}