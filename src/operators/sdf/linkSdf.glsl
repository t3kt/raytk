ReturnT thismap(CoordT p, ContextT ctx) {
	float len = THIS_Length;
	#ifdef THIS_HAS_INPUT_lengthField
	len *= inputOp_lengthField(p, ctx);
	#endif
	float radius = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	radius *= inputOp_radiusField(p, ctx);
	#endif
	float thick = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_thicknessField
	thick *= inputOp_thicknessField(p, ctx);
	#endif
	p -= THIS_Translate;
	vec3 q = vec3(p.x, max(abs(p.y)-len,0.0), p.z);
	return createSdf(length(vec2(length(q.xy)-radius,q.z)) - thick);
}