ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#else
	float h = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P2, p.THIS_PLANE_P1, p.THIS_AXIS);
	float d;
	BODY();
	return createSdf(d);
}