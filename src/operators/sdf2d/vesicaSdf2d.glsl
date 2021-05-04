ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	float d = THIS_Distance;
	p = abs(p);
	float b = sqrt(r*r-d*d);
	return createSdf(((p.y-b)*d>p.x*b) ? length(p-vec2(0.0,b)) : length(p-vec2(-d,0.0))-r);
}