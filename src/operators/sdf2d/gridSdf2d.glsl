ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	#ifdef THIS_HAS_INPUT_sizeField
	float sz = inputOp_sizeField(p0, ctx);
	#else
	float sz = THIS_Size;
	#endif
	vec4 result;
	vec2 id;
	p /= sz;
	SHAPE_BODY();
	// TODO: expose ID
	float distBorder = result.x;
	float distCenter = result.y;
	vec2 uv = result.zw;
	#ifdef THIS_HAS_INPUT_spacingField
	float sp = inputOp_spacingField(p0, ctx);
	#else
	float sp = THIS_Spacing;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p0, ctx);
	#else
	float r = THIS_Radius;
	#endif
	float d;
	FORMAT_BODY();
	Sdf res = createSdf(d * sz);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(uv, 1.));
	#endif
	return res;
}