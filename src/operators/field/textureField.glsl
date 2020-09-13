ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = (p.THIS_PLANE + THIS_Translate) / THIS_Scale;
	vec4 value = texture(THIS_texture, uv);
	#ifdef THIS_RETURN_TYPE_float
	return value.x;
	#else
	return value;
	#endif
}