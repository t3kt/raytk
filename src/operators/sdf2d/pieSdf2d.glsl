ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p, THIS_Rotate);
	vec2 c = THIS_C;
	float r = THIS_Radius;
	p.x = abs(p.x);
	float l = length(p) - r;
	float m = length(p-c*clamp(dot(p,c),0.0,r)); // c = sin/cos of the aperture
	return createSdf(max(l,m*sign(c.y*p.x-c.x*p.y)));
}