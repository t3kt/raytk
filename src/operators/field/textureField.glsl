ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_uvField)
	vec2 uv = inputOp_uvField(p, ctx).xy;
	#elif defined(THIS_COORD_TYPE_float)
	vec2 uv = vec2(p, 0);
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 uv = p;
	#else
	vec2 uv = getAxisPlane(p, int(THIS_Axis));
	#endif
	#ifdef THIS_Coordmode_uv
	uv = (uv - THIS_Translate) / THIS_Scale;
	vec4 range = vec4(-0.5, -0.5, 0.5, 0.5);
	switch (int(THIS_Extendmode)) {
		case THISTYPE_Extendmode_hold:
			uv = clamp(uv, range.xy, range.zw);
			break;
		case THISTYPE_Extendmode_repeat:
			uv = fract(uv+range.zw)+range.xy;
			break;
		case THISTYPE_Extendmode_mirror:
			uv = modZigZag(uv+range.zw)+range.xy;
			break;
		case THISTYPE_Extendmode_zero:
			if (uv.x < range.x || uv.x > range.z || uv.y < range.y || uv.y > range.w) {
				return THIS_asReturnT(0.);
			}
			break;
	}
	#endif
	vec4 value = vec4(0);
	#ifdef THIS_Coordmode_uv
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT) && defined(THIS_CONTEXT_TYPE_MaterialContext)
	value = textureLod(THIS_texture, uv + 0.5, ctx.lod);
	#else
	value = textureLod(THIS_texture, uv + 0.5, 0);
	#endif
	#elif defined(THIS_Coordmode_pixel)
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT) && defined(THIS_CONTEXT_TYPE_MaterialContext)
	value = texelFetch(THIS_texture, ivec2(  (uv)), ctx.lod);
	#else
	value = texelFetch(THIS_texture, ivec2(round(uv)), 0);
	#endif
	#else
	#error omgwtf
	#endif
	return THIS_asReturnT(value);
}