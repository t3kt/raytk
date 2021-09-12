ReturnT thismap(CoordT p, ContextT ctx) {
	float a = PI*(THIS_Bounces*p-1.0);
	return sin(a)/a;
}