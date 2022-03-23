ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 pos = p + THIS_Direction;
	vec3 col = THIS_Color * THIS_Intensity * clamp(dot(ctx.normal, THIS_Direction), 0., 1.);
	Light light = createLight(pos, col);
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#pragma r:if THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#pragma r:endif
	return light;
}

