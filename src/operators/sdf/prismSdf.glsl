ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	float h = inputOp1(p, ctx);
	#else
	float h = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_2
	float r = inputOp2(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P2, p.THIS_PLANE_P1, p.THIS_AXIS);
	return createSdf(THIS_EXPR);
}