void THIS_exposeSide(inout ContextT ctx, float i) {
	switch (THIS_Iterationtype) {
		case THIS_Iterationtype_sign:
			setIterationIndex(ctx, i);
			break;
		case THIS_Iterationtype_index:
			//  (-1, 1)  --> (1, 0)
			setIterationIndex(ctx, (i < 0) ? 1: 0);
			break;
	}
	#ifdef THIS_EXPOSE_sign
	THIS_sign = i;
	#endif
	#ifdef THIS_EXPOSE_index
	THIS_index = (i < 0) ? 1 : 0;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		THIS_exposeSide(ctx, 1.);
	} else {
		float shift = THIS_Shift;
		#ifdef THIS_HAS_INPUT_shiftField
		shift += inputOp_shiftField(p, ctx);
		#endif
		vec3 planeNormal;
		int axis;
		float dir;
		DIRECTION_BODY();
		#ifdef THIS_COORD_TYPE_vec2
		vec3 q = vec3(p, 0.);
		planeNormal.z = 0.;
		#else
		vec3 q = p;
		#endif
		planeNormal = normalize(planeNormal);
		q -= planeNormal * shift * dir;

		if (axis == -1) {
			float t = pReflect(q, planeNormal, 0.);
			THIS_exposeSide(ctx, t);
		} else {
			float q0 = getAxis(q, axis) * dir;
			THIS_exposeSide(ctx, sgn(q0));

			float b = THIS_Blend * THIS_Enableblend;
			q0 = sabs(q0, b);

			setAxis(q, axis, q0 * dir);
		}
		float offset = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		offset += inputOp_offsetField(p, ctx);
		#endif
		q -= planeNormal * offset * dir;

		#ifdef THIS_COORD_TYPE_vec2
		p = q.xy;
		#else
		p = q;
		#endif
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}
