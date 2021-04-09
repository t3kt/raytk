ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);

	vec3 col = goochShading(
		lightDir,
		viewDir,
		norm,
		THIS_Coolcolor, THIS_Warmcolor, THIS_Basecolor);

	#ifdef THIS_Uselightcolor
	col *= ctx.light.color;
	#endif

	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	col *= ctx.shadedLevel;
	#endif

	return vec4(col, 0.);
}