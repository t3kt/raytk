ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	#ifdef THIS_Useexponent
		return createSdf(fGDF(p - THIS_Translate, r, THIS_Exponent, int(THIS_BEGIN), int(THIS_END)));
	#else
		return createSdf(fGDF(p - THIS_Translate, r, int(THIS_BEGIN), int(THIS_END)));
	#endif
}