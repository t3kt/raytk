ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	p = vec2(length(p), atan(p.y, p.x));
	#elif defined(THIS_COORD_TYPE_vec3)
	p = THIS_EXPR;
	#else
	#error invalidCoordType
	#endif
	return inputOp1(p, ctx);
}
