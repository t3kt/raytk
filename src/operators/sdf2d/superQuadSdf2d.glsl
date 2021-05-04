ReturnT thismap(CoordT p, ContextT ctx) {
	float e = THIS_Exponent;
	p = abs(p);
	return createSdf(pow(pow(p.x,e)+pow(p.y,e),1./e)-THIS_Radius);
}