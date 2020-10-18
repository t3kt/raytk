ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdSolidAngle(
		p - THIS_Translate,
		vec2(THIS_Anglesin, THIS_Anglecos),
		THIS_Radius));
}