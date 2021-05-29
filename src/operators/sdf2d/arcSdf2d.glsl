// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/wl23RK
ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 sca = THIS_Sc.xz;
	vec2 scb = THIS_Sc.yw;
	float ra = THIS_Radius;
	float rb = THIS_Thickness;
	p *= mat2(sca.x,sca.y,-sca.y,sca.x);
	p.x = abs(p.x);
	float k = (scb.y*p.x>scb.x*p.y) ? dot(p,scb) : length(p);
	return createSdf(sqrt( dot(p,p) + ra*ra - 2.0*ra*k ) - rb);
}