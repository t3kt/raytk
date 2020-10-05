ReturnT thismap(CoordT p, ContextT ctx) {
	THIS_NOISE_COORD_TYPE q;
	#if defined(THIS_COORD_TYPE_vec2)
		#if defined(THIS_NOISE_COORD_vec2)
		q = p;
		#else
		q = THIS_NOISE_COORD_TYPE(0);
		q.THIS_PLANE = p;
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

	return THIS_FUNCTION(q);
}