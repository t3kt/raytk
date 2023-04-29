ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 dir = normalize(ctx.normal);
	vec3 pos = p + dir * RAYTK_MAX_DIST;
	vec3 col = THIS_Color * THIS_Intensity;
	Light light = createLight(pos, col);
	#ifdef THIS_EXPOSE_lightdir
	THIS_lightdir = normalize(light.pos - p);
	#endif
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#ifdef THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#endif
	return light;
}