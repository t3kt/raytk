ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_float
	float u = (p - THIS_Translate) / THIS_Scale;
	#else
	float u = (p.THIS_AXIS - THIS_Translate) / THIS_Scale;
	#endif
	#if defined(THIS_Extendmode_hold)
	u = clamp(u, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
	u = fract(u);
	#elif defined(THIS_Extendmode_mirror)
	u = modZigZag(u);
	#elif defined(THIS_Extendmode_zero)
		if (u < 0 || u > 1) {
			#if defined(THIS_RETURN_TYPE_float)
			return 0;
			#elif defined(THIS_RETURN_TYPE_Sdf)
			return createSdf(0);
			#else
			return vec4(0);
			#endif
		}
	#endif
	
	vec4 value = texture(THIS_texture, vec2(u, 0));
	#if defined(THIS_RETURN_TYPE_float)
	return value.x;
	#elif defined(THIS_RETURN_TYPE_Sdf)
	return createSdf(value.x);
	#else
	return value;
	#endif
}