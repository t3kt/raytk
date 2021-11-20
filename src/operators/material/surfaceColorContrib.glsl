ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = THIS_Defaultcolor;
	#pragma r:if RAYTK_USE_SURFACE_COLOR
		col = mix(col, ctx.result.color.rgb, ctx.result.color.w);
	#pragma r:endif
	return ReturnT(col, 0.);
}