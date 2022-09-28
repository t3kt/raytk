ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	float d = length(p) - r;
	ReturnT res = createSdf(d);
	#if defined(THIS_Uvmode_cartesian)
	assignUV(res, vec3(map01(p, -vec2(r/2.), vec2(r/2.)), 0.));
	#elif defined(THIS_Uvmode_polar)
	assignUV(res, vec3(
		length(p) / r,
		atan(p.y, p.x),
		0.
	));
	#elif defined(THIS_Uvmode_extparam) || defined(THIS_Uvmode_normextparam)
	// https://www.shadertoy.com/view/WldSWX
	float band = THIS_Externalbandsize;
	float ra = band*round(d/band);
	float l = (res.x+ra)*(atan(p.x,p.y)+PI);
	{
		#if defined(THIS_Uvmode_extparam)
		assignUV(res, vec3(l, d-ra, 0.));
		#elif defined(THIS_Uvmode_normextparam)
		float total = TAU*(d+ra);
		assignUV(res, vec3(l / total, d-ra, 0.));
		#endif
	}
	#endif
	return res;
}