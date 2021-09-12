ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q;
	BODY();
	return createSdf(fCorner(q - THIS_Translate));
}