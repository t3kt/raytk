ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdSuperQuad(abs(p), THIS_Exponent)-THIS_Radius);
}