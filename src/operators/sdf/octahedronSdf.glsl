ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	float d;
	BODY();
	return createSdf(d);
}