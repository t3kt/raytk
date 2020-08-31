ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(fBox(p - THIS_Translate, THIS_Scale));
}