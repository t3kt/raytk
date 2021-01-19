ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	return createSdf(sdHelix(
		p, THIS_Radius, THIS_Thickness, THIS_Spread, THIS_Dualspread * THIS_Radius));
}