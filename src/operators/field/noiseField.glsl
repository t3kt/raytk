ReturnT thismap(CoordT p, ContextT ctx) {
	THIS_NOISE_COORD_TYPE q;
	#if defined(THIS_COORD_TYPE_vec2)
		#if defined(THIS_NOISE_COORD_vec2)
		q = p;
		#elif defined(THIS_NOISE_COORD_vec3)
		q = vec3(p, 0);
		#elif defined(THIS_NOISE_COORD_vec4)
		q = vec4(p, 0., 0.);
		#else
		#error invalidNoiseCoordType
		#endif
	#elif defined(THIS_COORD_TYPE_vec3)
		#if defined(THIS_NOISE_COORD_vec2)
		q = p.THIS_PLANE;
		#elif defined(THIS_NOISE_COORD_vec3)
		q = p;
		#elif defined(THIS_NOISE_COORD_vec4)
		q = vec4(0);
		q.xyz = p;
		#endif
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;

	ReturnT val = THIS_FUNCTION(q);
	return (val * THIS_Amplitude) + THIS_Offset;
}