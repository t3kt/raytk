// https://www.shadertoy.com/view/Wdjfz3
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float ra = inputOp_radiusField(p, ctx);
	#else
	float ra = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_roundingField
	float rb = inputOp_roundingField(p, ctx);
	#else
	float rb = THIS_Rounding*ra;
	#endif
	#ifdef THIS_HAS_INPUT_point1Field
	vec2 a = adaptAsVec2(inputOp_point1Field(p, ctx));
	#else
	vec2 a = THIS_Point1;
	#endif
	#ifdef THIS_HAS_INPUT_point2Field
	vec2 b = adaptAsVec2(inputOp_point2Field(p, ctx));
	#else
	vec2 b = THIS_Point2;
	#endif
	#ifdef THIS_HAS_INPUT_bulgeField
	float tc = inputOp_bulgeField(p, ctx);
	#else
	float tc = THIS_Bulge;
	#endif
	float d;
	BODY();
	return createSdf(d);
}