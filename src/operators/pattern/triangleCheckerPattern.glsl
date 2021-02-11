ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;
	p.y = p.y * 0.866 + p.x * 0.5;
	if(fract(p.y) > fract(p.x)) return 1.0;
	return 0.0;
}