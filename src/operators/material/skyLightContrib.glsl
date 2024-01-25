ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 norm = normalize(ctx.normal);
	vec3 dir = normalize(THIS_Dir);
	pRotateOnXYZ(dir, THIS_Rotate);
	float amount = clamp(0.5+0.5*dot(normalize(ctx.normal), dir), 0, 1) * THIS_Level;
	#if defined(THIS_RETURN_TYPE_float)
	return amount;
	#elif defined(THIS_RETURN_TYPE_vec4)
	return vec4(amount * THIS_Color, 0.0);
	#else
	#error invalidReturnType
	#endif
}