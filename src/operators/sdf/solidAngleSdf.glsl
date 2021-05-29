ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec2 c = vec2(THIS_Anglesin, THIS_Anglecos);
	float ra = THIS_Radius;
	vec2 q = vec2( length(p.xz), p.y );
	float l = length(q) - ra;
	float m = length(q - c*clamp(dot(q,c),0.0,ra) );
	return createSdf(max(l,m*sign(c.y*q.x-c.x*q.y)));
}