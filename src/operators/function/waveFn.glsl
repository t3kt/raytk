ReturnT thismap(CoordT p, ContextT ctx) {
	p = (p / THIS_Period) + THIS_Phase;
	CoordT val = (THIS_FUNC(p) * THIS_Amplitude) + THIS_Offset;
	#if defined(THIS_COORD_TYPE_float)
	return val;
	#elif defined(THIS_COORD_TYPE_vec2)
	return vec4(val, 0., 0.);
	#elif defined(THIS_COORD_TYPE_vec3)
	return vec4(val, 0.);
	#else
	#error invalidCoordType
	#endif
}