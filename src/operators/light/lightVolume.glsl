float THIS_getLevel(CoordT p, ContextT ctx) {
	if (THIS_Level <= 0.) return 0.;
	#ifdef THIS_HAS_INPUT_1
		float d = inputOp1(p, ctx).x - THIS_Offset;
		return THIS_Level * (1.0 - smoothstep(0., THIS_Blending, max(d, 0.)));
	#else
	return THIS_Level;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = vec3(0.);
	float level = THIS_getLevel(p, ctx);
	if (level > 0.) {
		#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
		MaterialContext matCtx = createMaterialContext();
		matCtx.ray = ctx.ray;
		level *= calcShadedLevel(p, matCtx);
		#endif
	}
	if (level > 0.) {
		col = THIS_Color;
		#ifdef THIS_HAS_INPUT_2
		col *= fillToVec3(inputOp2(p, ctx));
		#endif
		col *= level;
	}
	return vec4(col, 1.);
}