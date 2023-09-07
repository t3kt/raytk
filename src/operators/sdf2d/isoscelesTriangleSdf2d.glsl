ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#else
	float h = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_widthField
	float w = inputOp_widthField(p, ctx);
	#else
	float w = THIS_Width;
	#endif
	DIRECTION_BODY();
	p.y *= -1.;
	POSITION_BODY();
	float d = sdTriangleIsosceles(p, vec2(w, h));
	return createSdf(d);
}