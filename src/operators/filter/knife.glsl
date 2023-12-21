ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		vec3 q = adaptAsVec3(p);
		AXIS_BODY();
		#if defined(THIS_COORD_TYPE_vec3)
		q *= rotateMatrix(THIS_Rotateplane);
		#elif defined(THIS_COORD_TYPE_vec2)
		pR(q.xy, THIS_Rotateplane.z);
		#else
		#error invalidCoordType
		#endif
		float o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx);
		#endif
		float plane = q.y - o;
		SIDE_BODY();
		#if defined(THIS_RETURN_TYPE_float)
		res = max(plane, res);
		#elif defined(THIS_RETURN_TYPE_Sdf)
		{
			if (IS_TRUE(THIS_Enablesmoothing)) {
				res.x = fOpIntersectionRound(res.x, plane, THIS_Smoothradius);
			} else {
				res.x = max(plane, res.x);
			}
		}
		#else
		#error invalidReturnType
		#endif
	}
	return res;
}