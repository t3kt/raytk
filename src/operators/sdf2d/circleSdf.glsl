ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	ReturnT res = createSdf(length(p)-r);
	#if defined(THIS_Uvmode_cartesian)
	assignUV(res, vec3(map01(p, -vec2(r/2.), vec2(r/2.)), 0.));
	#elif defined(THIS_Uvmode_polar)
	assignUV(res, vec3(
		length(p) / r,
		atan(p.y, p.x),
		0.
	));
	#endif
	return res;
}