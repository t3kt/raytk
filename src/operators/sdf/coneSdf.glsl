ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#ifdef THIS_HAS_INPUT_heightField
	float height = THIS_Height * inputOp_heightField(p, ctx);
	#else
	float height = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float radiusMod = inputOp_radiusField(p, ctx);
	#else
	const float radiusMod = 1.;
	#endif
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	ReturnT res;
	BODY();
	return res;
}