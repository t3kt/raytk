ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_uvField)
	vec2 uv = inputOp_uvField(p, ctx).xy;
	#elif defined(THIS_COORD_TYPE_float)
	vec2 uv = vec2(p, 0);
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 uv = p;
	#else
	vec2 uv = p.THIS_PLANE;
	#endif
	uv = (uv - THIS_Translate) / THIS_Scale;
	#if defined(THIS_Extendmode_hold)
	uv = clamp(uv, -0.5, 0.5);
	#elif defined(THIS_Extendmode_repeat)
	uv = fract(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_mirror)
	uv = modZigZag(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_zero)
		if (uv.x < -0.5 || uv.x > 0.5 || uv.y < -0.5 || uv.y > 0.5) {
			#if defined(THIS_RETURN_TYPE_float)
			return 0;
			#else
			return vec4(0);
			#endif
		}
	#endif
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT) && defined(THIS_CONTEXT_TYPE_MaterialContext)
	vec4 value = textureLod(THIS_texture, uv + 0.5, ctx.lod);
	#else
	vec4 value = texture(THIS_texture, uv + 0.5);
	#endif
	#ifdef THIS_RETURN_TYPE_float
	return value.x;
	#else
	return value;
	#endif
}