float THIS_getLevel(CoordT p, ContextT ctx, out vec4 surfaceColor) {
	if (THIS_Level <= 0.) return 0.;
	#ifdef THIS_HAS_INPUT_boundVolume
		Sdf res = inputOp_boundVolume(p, ctx);
		#if defined(THIS_Usesdfcolor) && defined(RAYTK_USE_SURFACE_COLOR)
		surfaceColor = res.color;
		#endif
		float d = res.x - THIS_Offset;
		return THIS_Level * (1.0 - max(0., smoothstep(-THIS_Blending*0.5, THIS_Blending*0.5, d)));
	#else
	return THIS_Level;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = vec3(0.);
	vec4 surfaceColor = vec4(0.);
	float level = THIS_getLevel(p, ctx, surfaceColor);
	if (level > 0.) {
		#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
		level *= ctx.shadedLevel;
		#endif
	}
	if (level > 0.) {
		col = THIS_Color;
		#ifdef THIS_Uselightcolor
		col *= ctx.light.color;
		#endif
		#ifdef THIS_Usesdfcolor
		col *= mix(vec3(1.), surfaceColor.rgb, surfaceColor.a);
		#endif
		#ifdef THIS_HAS_INPUT_colorField
		col *= fillToVec3(inputOp_colorField(p, ctx));
		#endif
		col *= level;
	}
	return vec4(col, 1.);
}