ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);

	vec3 col = goochShading(
		lightDir,
		viewDir,
		norm,
		THIS_Coolcolor * THIS_Level,
		THIS_Warmcolor * THIS_Level,
		THIS_Basecolor * THIS_Level);

	#pragma r:if THIS_Uselightcolor
	col *= ctx.light.color;
	#pragma r:endif

	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	col *= ctx.shadedLevel;
	#pragma r:endif

	return vec4(col, 0.);
}