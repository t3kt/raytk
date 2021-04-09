ReturnT thismap(CoordT p, ContextT ctx) {
	float u;
	#if defined(THIS_HAS_INPUT_1)
		u = inputOp1(p, ctx);
	#elif defined(THIS_COORD_TYPE_float)
		u = p;
	#elif defined(THIS_COORD_TYPE_vec2) && defined(THIS_Axis_z)
		u = p.x;
	#else
		u = p.THIS_Axis;
	#endif
	u = (u - THIS_Translate) / THIS_Scale;

	#if defined(THIS_Extendmode_hold)
		u = clamp(u, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
		u = fract(u);
	#elif defined(THIS_Extendmode_mirror)
		u = modZigZag(u);
	#elif defined(THIS_Extendmode_zero)
		if (u < 0 || u > 1) {
			ReturnT res;
			initDefVal(res);
			return res;
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