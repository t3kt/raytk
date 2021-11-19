ReturnT thismap(CoordT p, ContextT ctx) {
	float d = tdhooperHead(p);
	return createSdf(d);
}