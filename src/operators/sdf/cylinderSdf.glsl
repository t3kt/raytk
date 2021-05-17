ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec3 q = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	float r = THIS_Radius;
	#if defined(THIS_HAS_INPUT_1) && defined(inputOp1_COORD_TYPE_float)
	r *= inputOp1(q.y, ctx);
	#elif defined(THIS_HAS_INPUT_1) && defined(inputOp1_COORD_TYPE_vec3)
	r *= inputOp1(p, ctx);
	#endif
	float h = THIS_Height;
	#if defined(THIS_HAS_INPUT_2) && defined(inputOp2_COORD_TYPE_float)
	h *= inputOp2(q.y, ctx);
	#elif defined(THIS_HAS_INPUT_2) && defined(inputOp2_COORD_TYPE_vec3)
	h *= inputOp2(p, ctx);
	#endif
	return createSdf(fCylinder(q, r, h));
}