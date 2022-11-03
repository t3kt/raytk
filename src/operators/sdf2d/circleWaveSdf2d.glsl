// Circle Wave - distance by iq
// https://www.shadertoy.com/view/stGyzt

ReturnT thismap(CoordT p, ContextT ctx) {
	float tb = THIS_Curl;
	float ra = THIS_Radius;

	tb = PI*5.0/6.0 * max(tb,0.0001);
	vec2 co = ra*vec2(sin(tb),cos(tb));

	p.x = abs(mod(p.x,co.x*4.0)-co.x*2.0);

	vec2 p1 = p;
	vec2 p2 = vec2(abs(p.x-2.0*co.x),-p.y+2.0*co.y);
	float d1 = ((co.y*p1.x>co.x*p1.y) ? length(p1-co) : abs(length(p1)-ra));
	float d2 = ((co.y*p2.x>co.x*p2.y) ? length(p2-co) : abs(length(p2)-ra));

	float d = min( d1, d2) - THIS_Thickness;
	return createSdf(d);
}