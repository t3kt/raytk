ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(THIS_PRISM_FUNC(p - THIS_Translate, vec2(THIS_Radius, THIS_Height)));
}