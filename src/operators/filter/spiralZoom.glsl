ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	vec2 q = p;
	#elif defined(THIS_COORD_TYPE_vec3)
	vec2 q = p.THIS_PLANE;
	#else
	#error invalidCoordType
	#endif

	q = spiralZoom(
		q,
		THIS_Center,
		THIS_Branches,
		THIS_Twist,
		THIS_Zoom,
		THIS_Phase);

	#if defined(THIS_COORD_TYPE_vec2)
	return inputOp1(q, ctx);
	#elif defined(THIS_COORD_TYPE_vec3)
	p.THIS_PLANE = q;
	return inputOp1(p, ctx);
	#else
	#error invalidCoordType
	#endif
}
