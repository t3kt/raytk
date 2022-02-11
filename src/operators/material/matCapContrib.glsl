ReturnT thismap(CoordT p, ContextT ctx) {
	float level = THIS_Level * THIS_Enable;
	vec3 reflected = reflect(ctx.ray.dir, ctx.normal);
	float m = 2.8284271247461903 * sqrt( reflected.z+1.0 );
	vec2 uv = reflected.xy / m + 0.5;
	uv = clamp(uv, vec2(0.), vec2(1.));
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT) && defined(THIS_CONTEXT_TYPE_MaterialContext)
	vec4 value = textureLod(THIS_texture, uv, ctx.lod);
	#else
	vec4 value = texture(THIS_texture, uv);
	#endif
	value.rgb *= level;
	return value;
}