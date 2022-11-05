ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_beginEndField
	ivec2 be = ivec2(inputOp_beginEndField(p, ctx).xy);
	#else
	ivec2 be = ivec2(THIS_Begin, THIS_End);
	#endif
	#ifdef THIS_HAS_INPUT_exponentField
	float e = inputOp_exponentField(p, ctx);
	#else
	float e = THIS_Exponent;
	#endif
	BODY();
	float d;
	if (IS_TRUE(THIS_Useexponent)) {
		d = fGDF(p - THIS_Translate, r, e, be.x, be.y);
	} else {
		d = fGDF(p - THIS_Translate, r, be.x, be.y);
	}
	return createSdf(d);
}