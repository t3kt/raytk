ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	float amount = THIS_EXPR;
	#if defined(THIS_RETURN_TYPE_float)
	return amount;
	#elif defined(THIS_RETURN_TYPE_vec4)
	return vec4(amount * THIS_Color, 0.0);
	#else
	#error invalidReturnType
	#endif
}