ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdBoundingBox(p - THIS_Translate, THIS_Scale, THIS_Thickness));
}