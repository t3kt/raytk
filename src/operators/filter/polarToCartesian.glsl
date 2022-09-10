ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
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
