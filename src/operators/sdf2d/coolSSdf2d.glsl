// CoolS - distance by iq
// https://www.shadertoy.com/view/clVXWc

ReturnT thismap(CoordT p, ContextT ctx) {
	// symmetries
	float six = (p.y<0.0) ? -p.x : p.x; // float six = p.x*sign(p.y);
	p = abs(p);
	float rex = p.x - min(round(p.x/.4),.4);
	float aby = abs(p.y-.4);

	// 3 line segments are enough!
	float d; vec2 v;
	v=vec2(six,.2-p.y); v  -=clamp(.5*(v.x+v.y),.0,.4); d=      dot(v,v) ;
	v=vec2(p.x,.6-aby); v  -=clamp(.5*(v.x+v.y),.0,.4); d=min(d,dot(v,v));
	v=vec2(rex,p.y-.2); v.y-=clamp(v.y         ,.0,.4); d=min(d,dot(v,v));

	// interior vs exterior
	//float s = p.x - min(min(1.-p.y,.4),.2+p.y);
	float s = 2.0*p.x - 1.0 + aby + abs(aby-.2);

	return createSdf(sqrt(d) * sign(s));
}