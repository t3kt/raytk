vec4 thismap(CoordT p, ContextT ctx) {
#ifdef THIS_COORD_TYPE_vec2
	return vec4(p, 0, 0);
#else
	return vec4(p, 0);
#endif
}