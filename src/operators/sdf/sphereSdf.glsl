ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_1
	r *= inputOp1(p, ctx);
	#endif
	p -= THIS_Translate;
	ReturnT res = createSdf(length(p)-r);
	#if defined(THIS_Uvmode_bounds)
	assignUV(res, map01(p, vec3(-r), vec3(r)));
	#elif defined(THIS_Uvmode_spherical)
	assignUV(
		res,
		vec3(
			res.x,
			acos(p.z / res.x),
			atan(p.y, p.x)
		));
	#endif
	return res;
}