// Spike distance by dracusa
// https://www.shadertoy.com/view/3ssSR7

ReturnT thismap(CoordT p, ContextT ctx) {
	p.y -= THIS_Offset;
	float h = THIS_Height;
	float d = p.y - (h*0.1)/(abs(p.x)+0.1);
	d = min(d, length(p - vec2(0., min(h, p.y))));
	float d2 = abs(p.x) - ((h*0.1)-0.1*p.y)/p.y;
	if (p.y<h && d>0.0)
	d = min(d, d2);
	return createSdf(d);
}