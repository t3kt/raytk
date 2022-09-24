ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	p -= THIS_Translate;
	ReturnT res = createSdf(length(p)-r);
	#if defined(THIS_Uvmode_bounds)
	assignUV(res, map01(p, vec3(-r), vec3(r)));
	#elif defined(THIS_Uvmode_sphericalpolar)
	assignUV(
		res,
		vec3(
			res.x,
			acos(p.z / res.x),
			atan(p.y, p.x)
		));
	#elif defined(THIS_Uvmode_sphere)
	CoordT q = p / r;
	// https://www.shadertoy.com/view/3dVSzm
	assignUV(
		res,
		vec3(
			0.5 + atan(q.z, q.x) / TAU,
			0.5 - asin(q.y) / PI,
			0.
		)
	);
	#endif
	return res;
}