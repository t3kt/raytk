ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return vec4(0.); }
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	float level = THIS_Level;

	#ifdef THIS_HAS_INPUT_baseColorField
	vec3 baseColor = fillToVec3(inputOp_baseColorField(p, ctx));
	#else
	vec3 baseColor = THIS_Basecolor;
	#endif
	#ifdef THIS_HAS_INPUT_warmColorField
	vec3 warmColor = fillToVec3(inputOp_warmColorField(p, ctx));
	#else
	vec3 warmColor = THIS_Warmcolor;
	#endif
	#ifdef THIS_HAS_INPUT_coolColorField
	vec3 coolColor = fillToVec3(inputOp_coolColorField(p, ctx));
	#else
	vec3 coolColor = THIS_Coolcolor;
	#endif

	vec3 col = goochShading(
		lightDir,
		viewDir,
		norm,
		coolColor * level,
		warmColor * level,
		baseColor * level);

	#ifdef THIS_Uselightcolor
	col *= ctx.light.color;
	#endif

	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	col *= ctx.shadedLevel;
	#endif

	return vec4(col, 0.);
}