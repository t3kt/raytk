ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = (p.THIS_PLANE - THIS_Translate) / THIS_Scale;
	#if defined(THIS_Extend_hold)
	uv = clamp(uv, 0, 1);
	#elif defined(THIS_Extend_repeat)
	uv = fract(uv);
	#elif defined(THIS_Extend_mirror)
	uv = modZigZag(uv);
	#elif defined(THIS_Extend_zero)
		if (uv.x < 0 || uv.x > 1 || uv.y < 0 || uv.y > 1) {
			#if defined(THIS_RETURN_TYPE_float)
			return 0;
			#elif defined(THIS_RETURN_TYPE_Sdf)
			return createSdf(0);
			#else
			return vec4(0);
			#endif
		}
	#endif
	
	vec4 value = texture(THIS_texture, uv);
	#ifdef THIS_RETURN_TYPE_float
	return value.x;
	#else
	return value;
	#endif
}