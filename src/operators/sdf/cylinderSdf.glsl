ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	return createSdf(fCylinder(p, THIS_Radius, THIS_Height));
}