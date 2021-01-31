ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;
	p = 0.5 - fract(p);
	return 0.5 + 0.5*sign(p.x*p.y);
}