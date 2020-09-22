Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(sdLink(p - THIS_Translate, THIS_Length, THIS_Radius, THIS_Thickness));
}