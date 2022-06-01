ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p, THIS_Rotate);
	#ifdef THIS_HAS_INPUT_angleField
	float a = radians(inputOp_angleField(p, ctx));
	#else
	float a = THIS_Angle;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = map01(atan(p.y, p.x), a, 0.);
	#endif
	vec2 c = vec2(sin(a * .5), cos(a * .5));
	vec2 r = vec2(THIS_Radius, THIS_Innerradius);
	#ifdef THIS_HAS_INPUT_radiusField
	r *= fillToVec2(inputOp_radiusField(p, ctx));
	#endif
	p.x = abs(p.x);
	float l = length(p) - r.x;
	float m;
	m = length(p-c*clamp(dot(p,c),0.0,r.x));
	float d;
//	float m = length(p-c*dot(p,c));
//	float d = m*sign(c.y*p.x-c.x*p.y);
	BODY();
	return createSdf(d);
}