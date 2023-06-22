ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 s = THIS_Size;
	#ifdef THIS_HAS_INPUT_sizeField
	s *= fillToVec3(inputOp_sizeField(p, ctx));
	#endif
	float r = THIS_Smoothradius;
	#ifdef THIS_HAS_INPUT_smoothRadiusField
	r *= inputOp_smoothRadiusField(p, ctx);
	#endif
	vec3 l = THIS_Length;
	#ifdef THIS_HAS_INPUT_lengthField
	l *= fillToVec3(inputOp_lengthField(p, ctx));
	#endif
	p -= THIS_Translate;
	float d;
	BODY();
	SHAPE();
	return createSdf(d);
}