ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = THIS_Defaultcolor;
	#if defined(RAYTK_USE_SURFACE_COLOR)
		col = mix(col, ctx.result.color.rgb, ctx.result.color.w);
	#endif
	return ReturnT(col, 0.);
}