ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_beginEndField
	vec2 beginEnd = inputOp_beginEndField(p, ctx).xy;
	#endif
	float d;
	if (IS_TRUE(THIS_Useexponent)) {
		d = fGDF(p - THIS_Translate, r, THIS_Exponent, int(THIS_BEGIN), int(THIS_END));
	} else {
		d = fGDF(p - THIS_Translate, r, int(THIS_BEGIN), int(THIS_END));
	}
	return createSdf(d);
}