ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		#if defined(THIS_COORD_TYPE_vec2)
		p = vec2(p.x * cos(p.y), p.x * sin(p.y));
		#elif defined(THIS_COORD_TYPE_vec3)
		BODY();
		#else
		#error invalidCoordType
		#endif
	}
	return inputOp1(p, ctx);
}
