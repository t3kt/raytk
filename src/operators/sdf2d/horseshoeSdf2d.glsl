// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/WlSGW1
ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 c = THIS_Sc;
	float r = THIS_Radius;
	vec2 w = vec2(THIS_Length, THIS_Thickness);
	p.x = abs(p.x);
	float l = length(p);
	p = mat2(-c.x, c.y, c.y, c.x)*p;
	p = vec2((p.y>0.0)?p.x:l*sign(-c.x),
	(p.x>0.0)?p.y:l );
	p = vec2(p.x,abs(p.y-r))-w;
	return createSdf(length(max(p,0.0)) + min(0.0,max(p.x,p.y)));
}