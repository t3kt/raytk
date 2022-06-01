ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (THIS_Enable < 0.5) {
		res = inputOp1(p, ctx);
	} else {
		#if defined(THIS_COORD_TYPE_vec3)
		float plane = (p * rotateMatrix(radians(THIS_Rotateplane))).y - THIS_Offset;
		#elif defined(THIS_COORD_TYPE_vec2)
		vec2 q = p;
		pR(q, THIS_Rotateplane.z);
		float plane = q.y - THIS_Offset;
		#else
		#error invalidCoordType
		#endif
		res = inputOp1(p, ctx);
		#ifdef THIS_Side_above
		plane *= -1.;
		#endif
		#if defined(THIS_RETURN_TYPE_float)
		res = max(plane, res);
		#elif defined(THIS_RETURN_TYPE_Sdf)
		res.x = max(plane, res.x);
		#else
		#error invalidReturnType
		#endif
	}
	return res;
}