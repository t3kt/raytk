ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(THIS_SHAPE_FUNC(p - THIS_Translate, THIS_Radius));
}