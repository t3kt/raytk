Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(fDisc(p - THIS_Translate, THIS_Radius));
}