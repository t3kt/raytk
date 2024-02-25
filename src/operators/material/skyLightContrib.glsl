ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 norm = normalize(ctx.normal);
	#ifdef THIS_HAS_INPUT_directionField
	vec3 dir = normalize(inputOp_directionField(p, ctx).xyz);
	#else
	vec3 dir = normalize(THIS_Dir);
	#endif
	vec3 rot = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_rotateField
	rot += radians(inputOp_rotateField(p, ctx).xyz);
	#endif
	pRotateOnXYZ(dir, rot);
	float amount = clamp(0.5+0.5*dot(normalize(ctx.normal), dir), 0, 1) * THIS_Level;
	#if defined(THIS_RETURN_TYPE_float)
	return amount;
	#elif defined(THIS_RETURN_TYPE_vec4)
	vec3 col = THIS_Color;
	#ifdef THIS_HAS_INPUT_colorField
	col *= fillToVec3(inputOp_colorField(p, ctx));
	#endif
	return vec4(amount * col, 0.0);
	#else
	#error invalidReturnType
	#endif
}