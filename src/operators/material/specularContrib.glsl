ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	float amount;
	BODY();
	amount *= THIS_Level;
	ReturnT res;
	#if defined(THIS_RETURN_TYPE_float)
	res = ReturnT(amount);
	#elif defined(THIS_RETURN_TYPE_vec4)
	{
		res = vec4(amount * THIS_Color, 0.0);
		#ifdef THIS_Uselightcolor
		res.rgb *= ctx.light.color;
		#endif
		#ifdef RAYTK_USE_SURFACE_COLOR
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