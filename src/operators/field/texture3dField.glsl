ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_coordField)
	vec3 uv = adaptAsVec3(inputOp_coordField(p, ctx));
	#elif defined(THIS_CONTEXT_TYPE_RayContext)
	vec3 uv = ctx.ray.dir;
	#else
	vec3 uv = adaptAsVec3(p);
	#endif
	uv = (uv - THIS_Translate) / THIS_Scale;
	ZMODE();
	#if defined(THIS_Extendmode_hold)
	uv = clamp(uv, -0.5, 0.5);
	#elif defined(THIS_Extendmode_repeat)
	uv = fract(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_mirror)
	uv = modZigZag(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_zero)
	if (uv.x < -0.5 || uv.x > 0.5 || uv.y < -0.5 || uv.y > 0.5 || uv.z < -0.5 || uv.z > 0.5) {
		return THIS_asReturnT(0.);
	}
	#endif
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT) && defined(THIS_CONTEXT_TYPE_MaterialContext)
	vec4 value = textureLod(THIS_texture, uv + 0.5, ctx.lod);
	#else
	vec4 value = texture(THIS_texture, uv + 0.5);
	#endif
	return THIS_asReturnT(value);
}