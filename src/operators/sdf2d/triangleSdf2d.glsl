ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_sizeField
	vec2 sz = fillToVec2(inputOp_sizeField(p, ctx));
	#else
	vec2 sz = vec2(THIS_Width, THIS_Height);
	#endif
	float d;
	BODY();
	return createSdf(d);
}