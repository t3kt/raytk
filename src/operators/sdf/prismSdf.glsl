ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P2, p.THIS_PLANE_P1, p.THIS_AXIS);
	return createSdf(THIS_EXPR);
}