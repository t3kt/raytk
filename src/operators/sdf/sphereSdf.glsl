ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	p -= THIS_Translate;
	ReturnT res = createSdf(length(p)-r);
	#pragma r:if THIS_Uvmode_bounds
	assignUV(res, map01(p, vec3(-r), vec3(r)));
	#pragma r:elif THIS_Uvmode_sphericalpolar
	assignUV(
		res,
		vec3(
			res.x,
			acos(p.z / res.x),
			atan(p.y, p.x)
		));
	#pragma r:elif THIS_Uvmode_sphere
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
	#pragma r:endif
	return res;
}