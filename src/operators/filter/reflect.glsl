void THIS_exposeSide(inout ContextT ctx, float i) {
	#pragma r:if THIS_Iterationtype_sign
	setIterationIndex(ctx, i);
	#pragma r:elif THIS_Iterationtype_index
	//  (-1, 1)  --> (1, 0)
	setIterationIndex(ctx, (i < 0) ? 1: 0);
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_sign
	THIS_sign = i;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_index
	THIS_index = (i < 0) ? 1 : 0;
	#pragma r:endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable <= 0.5) {
		THIS_exposeSide(ctx, 1.);
	} else {
		float shift = THIS_Shift;
		#pragma r:if THIS_HAS_INPUT_shiftField
		shift += inputOp_shiftField(p, ctx);
		#pragma r:endif
		vec3 planeNormal;
		int axis;
		float dir;
		DIRECTION_BODY();
		#pragma r:if THIS_COORD_TYPE_vec2
		vec3 q = vec3(p, 0.);
		planeNormal.z = 0.;
		#pragma r:else
		vec3 q = p;
		#pragma r:endif
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
		#pragma r:if THIS_HAS_INPUT_offsetField
		offset += inputOp_offsetField(p, ctx);
		#pragma r:endif
		q -= planeNormal * offset * dir;

		#pragma r:if THIS_COORD_TYPE_vec2
		p = q.xy;
		#pragma r:else
		p = q;
		#pragma r:endif
	}
	ReturnT res;
	#pragma r:if THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#pragma r:else
	res = adaptAsVec4(p);
	#pragma r:endif
	return res;
}
