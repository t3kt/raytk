ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 dir = normalize(THIS_Direction);
	pRotateOnXYZ(dir, THIS_Rotate);
	vec3 pos = p + dir * RAYTK_MAX_DIST;
	vec3 col = THIS_Color * THIS_Intensity * clamp(dot(ctx.normal, dir), 0., 1.);
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

