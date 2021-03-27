ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	float amount = clamp(0.5+0.5*dot(normalize(ctx.normal), THIS_Dir), 0, 1) * THIS_Level;
	#if defined(THIS_RETURN_TYPE_float)
	return amount;
	#elif defined(THIS_RETURN_TYPE_vec4)
	return vec4(amount * THIS_Color, 0.0);
	#else
	#error invalidReturnType
	#endif
}