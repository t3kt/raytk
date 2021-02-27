Sdf thismap(CoordT p, ContextT ctx) {
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	return createSdf(fDisc(p - THIS_Translate, THIS_Radius) - THIS_Thickness);
}