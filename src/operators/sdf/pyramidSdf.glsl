ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdPyramid(p - THIS_Translate, THIS_Height));
}