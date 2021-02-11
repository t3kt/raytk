Light thismap(vec3 p, LightContext ctx) {
	Light light;
	light.pos = p + THIS_Direction;
	light.color = THIS_Color * clamp(dot(ctx.normal, THIS_Direction), 0., 1.);
	return light;
}

