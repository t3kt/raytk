ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 d = abs(p - THIS_Translate)-THIS_Scale;
	return createSdf(length(max(d,0.0)) + min(max(d.x,d.y),0.0));
}