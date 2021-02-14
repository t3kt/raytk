ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	vec3 q = vec3(p, 0.);
	#elif defined(THIS_COORD_TYPE_vec3)
	vec3 q = p;
	#else
	#error invalidCoordType
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;

	vec3 val = curlNoise(q);
	return vec4((val * THIS_Amplitude) + THIS_Offset, 0.);
}