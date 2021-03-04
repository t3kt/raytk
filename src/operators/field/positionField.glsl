ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_RETURN_TYPE_float)
		#ifdef THIS_COORD_TYPE_float
			return p;
		#else
			return p.x;
		#endif
	#else
		#if defined(THIS_COORD_TYPE_float)
			return vec4(p, 0, 0, 0);
		#elif defined(THIS_COORD_TYPE_vec2)
			return vec4(p, 0, 0);
		#elif defined(THIS_COORD_TYPE_vec3)
			return vec4(p, 0);
		#else
			#error invalidCoordType
		#endif
	#endif
}