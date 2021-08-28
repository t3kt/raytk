float THIS_getLevel(CoordT p, ContextT ctx) {
	if (THIS_Level <= 0.) return 0.;
	#ifdef THIS_HAS_INPUT_1
		float d = inputOp1(p, ctx).x;
		return THIS_Level * step(0., -d);
	#else
	return THIS_Level;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = vec3(0.);
	float level = THIS_getLevel(p, ctx);
	if (level >= 0.) {
		#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
		MaterialContext matCtx = createMaterialContext();
		matCtx.ray = ctx.ray;
		level *= calcShadedLevel(p, matCtx);
		#endif
	}
	col = THIS_Color * level;
	return vec4(col, 1.);
}