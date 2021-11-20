float THIS_getLevel(CoordT p, ContextT ctx, out vec4 surfaceColor) {
	if (THIS_Level <= 0.) return 0.;
	#pragma r:if THIS_HAS_INPUT_boundVolume
		Sdf res = inputOp_boundVolume(p, ctx);
		#pragma r:if THIS_Usesdfcolor && RAYTK_USE_SURFACE_COLOR
		surfaceColor = res.color;
		#pragma r:endif
		float d = res.x - THIS_Offset;
		return THIS_Level * (1.0 - max(0., smoothstep(-THIS_Blending*0.5, THIS_Blending*0.5, d)));
	#pragma r:else
	return THIS_Level;
	#pragma r:endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 col = vec3(0.);
	vec4 surfaceColor = vec4(0.);
	float level = THIS_getLevel(p, ctx, surfaceColor);
	if (level > 0.) {
		#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
		level *= ctx.shadedLevel;
		#pragma r:endif
	}
	if (level > 0.) {
		col = THIS_Color;
		#pragma r:if THIS_Uselightcolor
		col *= ctx.light.color;
		#pragma r:endif
		#pragma r:if THIS_Usesdfcolor
		col *= mix(vec3(1.), surfaceColor.rgb, surfaceColor.a);
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_colorField
		col *= fillToVec3(inputOp_colorField(p, ctx));
		#pragma r:endif
		col *= level;
	}
	return vec4(col, 1.);
}