ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		vec3 q = adaptAsVec3(p);
		AXIS_BODY();
		#if defined(THIS_COORD_TYPE_vec3)
		q *= rotateMatrix(radians(THIS_Rotateplane));
		#elif defined(THIS_COORD_TYPE_vec2)
		pR(q.xy, radians(THIS_Rotateplane.z));
		#else
		#error invalidCoordType
		#endif
		#ifdef THIS_HAS_INPUT_offsetField
		float o = inputOp_offsetField(p, ctx);
		#else
		float o = THIS_Offset;
		#endif
		float plane = q.y - o;
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