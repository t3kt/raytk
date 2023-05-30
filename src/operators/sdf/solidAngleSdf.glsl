ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float ra = inputOp_radiusField(p, ctx);
	#else
	float ra = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_angleField
	float a = radians(inputOp_angleField(p, ctx));
	#else
	float a = THIS_Angle;
	#endif
	vec2 c = vec2(sin(a), cos(a));
	p -= THIS_Translate;
	vec2 q = vec2( length(p.xz), p.y );
	float l = length(q) - ra;
	float m = length(q - c*clamp(dot(q,c),0.0,ra) );
	return createSdf(max(l,m*sign(c.y*q.x-c.x*q.y)));
}