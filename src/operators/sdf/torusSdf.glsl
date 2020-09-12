ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(fTorus(p - THIS_Translate, THIS_Thickness, THIS_Radius));
}