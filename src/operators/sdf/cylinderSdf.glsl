ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(fCylinder(p - THIS_Translate, THIS_Radius, THIS_Height));
}