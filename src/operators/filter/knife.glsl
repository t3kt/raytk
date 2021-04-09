ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec3)
	float plane = (p * rotateMatrix(radians(THIS_Rotateplane))).y - THIS_Offset;
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 q = p;
	pR(q, THIS_Rotateplanez);
	float plane = q.y - THIS_Offset;
	#else
	#error invalidCoordType
	#endif
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_Side_above
	plane *= -1.;
	#endif
	#if defined(THIS_RETURN_TYPE_float)
	return max(plane, res);
	#elif defined(THIS_RETURN_TYPE_Sdf)
	res.x = max(plane, res.x);
	return res;
	#else
	#error invalidReturnType
	#endif
}