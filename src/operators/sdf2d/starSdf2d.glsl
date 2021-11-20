ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	float r = THIS_Radius;
	float n = THIS_Points;
	float t = THIS_Tightness;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_tightnessField
	t *= inputOp_tightnessField(p, ctx);
	#pragma r:endif
	float m = mapRange(t, 0., 1., 2., n);
	// next 4 lines can be precomputed for a given shape
	float an = PI/n;
	float en = PI/m;  // m is between 2 and n
	vec2  acs = vec2(cos(an),sin(an));
	vec2  ecs = vec2(cos(en),sin(en)); // ecs=vec2(0,1) for regular polygon,

	float bn = mod(atan(p.x,p.y),2.0*an) - an;
	p = length(p)*vec2(cos(bn),abs(sin(bn)));
	p -= r*acs;
	p += ecs*clamp( -dot(p,ecs), 0.0, r*acs.y/ecs.y);
	ReturnT res = createSdf(length(p)*sign(p.x));
	#pragma r:if THIS_Uvmode_cartesian
	assignUV(res, vec3(map01(p0, -vec2(THIS_Radius/2.), vec2(THIS_Radius/2.)), 0.));
	#pragma r:elif THIS_Uvmode_polar
	assignUV(res, vec3(
		length(p0) / THIS_Radius,
		atan(p0.y, p0.x),
		0.
	));
	#pragma r:endif
	return res;
}