ReturnT thismap(CoordT p, ContextT ctx) {
	Light light;
	light.pos = p + THIS_Direction;
	light.color = THIS_Color * THIS_Intensity * clamp(dot(ctx.normal, THIS_Direction), 0., 1.);
	#pragma r:if THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#pragma r:endif
	return light;
}

