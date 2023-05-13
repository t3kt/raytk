ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return ReturnT(0.);

	vec3 n = ctx.normal;
	vec3 v = normalize(-ctx.ray.dir);
	n *= TDRotateToVector(v, vec3(0., 1., 0.));
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(n.y, n.x)/TAU + 0.5;
	#endif

	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_blendingField
	float bl = inputOp_blendingField(p, ctx);
	#else
	float bl = THIS_Blending;
	#endif

	bl *= .5;
	float amount = n.z;
	amount = saturate(1.-smoothstep(th-bl, th+bl, amount));
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
		#ifdef RAYTK_USE_SURFACE_COLOR
		if (THIS_Usesurfacecolor) {
			res.rgb *= mix(vec3(1.), ctx.result.color.rgb, ctx.result.color.a);
		}
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