ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	float d = length(p) - r;
	ReturnT res = createSdf(d);
	#pragma r:if THIS_Uvmode_cartesian
	assignUV(res, vec3(map01(p, -vec2(r/2.), vec2(r/2.)), 0.));
	#pragma r:elif THIS_Uvmode_polar
	assignUV(res, vec3(
		length(p) / r,
		atan(p.y, p.x),
		0.
	));
	#pragma r:elif THIS_Uvmode_extparam || THIS_Uvmode_normextparam
	// https://www.shadertoy.com/view/WldSWX
	float band = THIS_Externalbandsize;
	float ra = band*round(d/band);
	float l = (res.x+ra)*(atan(p.x,p.y)+PI);
	{
		#pragma r:if THIS_Uvmode_extparam
		assignUV(res, vec3(l, d-ra, 0.));
		#pragma r:elif THIS_Uvmode_normextparam
		float total = TAU*(d+ra);
		assignUV(res, vec3(l / total, d-ra, 0.));
		#pragma r:endif
	}
	#pragma r:endif
	return res;
}