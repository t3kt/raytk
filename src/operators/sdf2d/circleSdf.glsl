ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	ReturnT res = createSdf(length(p)-r);
	#pragma r:if THIS_Uvmode_cartesian
	assignUV(res, vec3(map01(p, -vec2(r/2.), vec2(r/2.)), 0.));
	#pragma r:elif THIS_Uvmode_polar
	assignUV(res, vec3(
		length(p) / r,
		atan(p.y, p.x),
		0.
	));
	#pragma r:endif
	return res;
}