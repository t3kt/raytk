ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 scale = THIS_Scale;
	#ifdef THIS_HAS_INPUT_1
	scale *= vec3(inputOp1(p, ctx));
	#endif
	float thickness = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_2
	thickness *= inputOp2(p, ctx);
	#endif
	return createSdf(sdBoundingBox(p - THIS_Translate, scale, thickness));
}