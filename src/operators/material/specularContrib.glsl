ReturnT THIS_calc(
	CoordT p, ContextT ctx,
	float shininess, float roughness, float fresnel
) {
	if (ctx.light.absent) {return ReturnT(0);}
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);

	float amount;
	BODY();

	ReturnT res;
	#if defined(THIS_RETURN_TYPE_float)
	res = ReturnT(amount);
	#elif defined(THIS_RETURN_TYPE_vec4)
	res = vec4(vec3(amount), 0.0);
	if (IS_TRUE(THIS_Uselightcolor)) {
		res.rgb *= ctx.light.color;
	}
	#else
	#error invalidReturnType
	#endif

	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res *= ctx.shadedLevel;
	#endif
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return ReturnT(0.);

	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	#ifdef THIS_HAS_INPUT_shininessField
	float shininess = inputOp_shininessField(p, ctx);
	#else
	float shininess = THIS_Shininess;
	#endif
	#ifdef THIS_HAS_INPUT_roughnessField
	float roughness = inputOp_roughnessField(p, ctx);
	#else
	float roughness = THIS_Roughness;
	#endif
	#ifdef THIS_HAS_INPUT_fresnelField
	float fresnel = inputOp_fresnelField(p, ctx);
	#else
	float fresnel = THIS_Fresnel;
	#endif
	ReturnT res = ReturnT(0);
	res = THIS_calc(p, ctx, shininess, roughness, fresnel);
	#if defined(THIS_RETURN_TYPE_vec4)
	{
		res.rgb *= THIS_Color;
		#ifdef THIS_HAS_INPUT_colorField
		res.rgb *= fillToVec3(inputOp_colorField(p, ctx));
		#endif
		#ifdef RAYTK_USE_SURFACE_COLOR
		if (IS_TRUE(THIS_Usesurfacecolor)) {
			res.rgb *= mix(vec3(1.), ctx.result.color.rgb, ctx.result.color.a);
		}
		#endif
	}
	#endif
	res *= THIS_Level;
	return res;
}