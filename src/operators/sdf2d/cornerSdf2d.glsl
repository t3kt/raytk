ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = THIS_EXPR;
	return createSdf(fCorner(q - THIS_Translate));
}