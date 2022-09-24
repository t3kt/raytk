ReturnT thismap(CoordT p, ContextT ctx) {
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
	float amount;
	BODY();
	amount *= THIS_Level;
	ReturnT res;
	#if defined(THIS_RETURN_TYPE_float)
	res = ReturnT(amount);
	#elif defined(THIS_RETURN_TYPE_vec4)
	{
		res = vec4(amount * THIS_Color, 0.0);
		#ifdef THIS_HAS_INPUT_colorField
		res.rgb *= fillToVec3(inputOp_colorField(p, ctx));
		#endif
		#ifdef THIS_Uselightcolor
		res.rgb *= ctx.light.color;
		#endif
		#if defined(THIS_Usesurfacecolor) && defined(RAYTK_USE_SURFACE_COLOR)
		res.rgb *= mix(vec3(1.), ctx.result.color.rgb, ctx.result.color.a);
		#endif
	}
	#else
	#error invalidReturnType
	#endif
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res *= ctx.shadedLevel;
	#endif
	return res;
}