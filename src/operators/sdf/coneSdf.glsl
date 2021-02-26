Sdf thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#ifdef THIS_HAS_INPUT_1
	float height = THIS_Height * inputOp1(p, ctx);
	#else
	float height = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_2
	float radiusMod = inputOp2(p, ctx);
	#else
	const float radiusMod = 1.;
	#endif
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	return createSdf(THIS_EXPR);
}