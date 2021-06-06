ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	ReturnT res = createSdf(length(p)-THIS_Radius);
	#if defined(THIS_Uvmode_cartesian)
	assignUV(res, vec3(map01(p, -vec2(THIS_Radius/2.), vec2(THIS_Radius/2.)), 0.));
	#elif defined(THIS_Uvmode_polar)
	assignUV(res, vec3(
		length(p) / THIS_Radius,
		atan(p.y, p.x),
		0.
	));
	#endif
	return res;
}