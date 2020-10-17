Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(fCone(p - THIS_Translate, THIS_Radius, THIS_Height));
}