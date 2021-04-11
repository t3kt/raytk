// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/7dlGRf
ReturnT thismap(CoordT p, ContextT ctx) {
	float wi = THIS_Width;
	float he = THIS_Height;
	float sk = THIS_Skew;
	vec2 e = vec2(sk,he);
	p = (p.y<0.0)?-p:p;
	vec2  w = p - e; w.x -= clamp(w.x,-wi,wi);
	vec2  d = vec2(dot(w,w), -w.y);
	float s = p.x*e.y - p.y*e.x;
	p = (s<0.0)?-p:p;
	vec2  v = p - vec2(wi,0); v -= e*clamp(dot(v,e)/dot(e,e),-1.0,1.0);
	d = min( d, vec2(dot(v,v), wi*he-abs(s)));
	return createSdf(sqrt(d.x)*sign(-d.y));
}