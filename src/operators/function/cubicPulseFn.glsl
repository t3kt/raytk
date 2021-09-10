ReturnT thismap(CoordT p, ContextT ctx) {
	float x = p;
	float c = THIS_Phase;
	float w = THIS_Width;
	x = abs(x - c);
	if (x>w) return 0.0;
	x /= w;
	return 1.0 - x*x*(3.0-2.0*x);
}