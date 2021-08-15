ReturnT thismap(CoordT p, ContextT ctx) {
	return domainColoring(
		p,
		THIS_Gridspacing,
		THIS_Saturation,
		THIS_Gridstrength,
		THIS_Magstrength,
		THIS_Linepower
	);
}