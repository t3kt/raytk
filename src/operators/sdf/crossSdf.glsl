ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sizeField
	vec3 s = THIS_Size * fillToVec3(inputOp_sizeField(p, ctx));
	#else
	vec3 s = THIS_Size;
	#endif
	#ifdef THIS_HAS_INPUT_smoothRadiusField
	float r = THIS_Smoothradius * inputOp_smoothRadiusField(p, ctx);
	#else
	float r = THIS_Smoothradius;
	#endif
	p -= THIS_Translate;
	float d;
	BODY();
	return createSdf(d);
}