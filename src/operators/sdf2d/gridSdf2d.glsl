ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 result;
	vec2 id;
	BODY();
	// TODO: expose ID
	// TODO: UV
	float distBorder = result.x;
	float distCenter = result.y;
	vec2 uv = result.zw;
	float th = THIS_Thickness;
	Sdf res = createSdf(-distBorder + th);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(uv, 1.));
	#endif
	return res;
}