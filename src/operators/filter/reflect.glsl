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
	#pragma r:if THIS_Direction_custom
	vec3 planeNormal = THIS_Planenormal;
	#pragma r:else
	vec3 planeNormal = THIS_AXIS_VEC * THIS_DIR;
	#pragma r:endif
	#pragma r:if THIS_COORD_TYPE_vec2
	vec3 q = vec3(p, 0.);
	planeNormal.z = 0.;
	#pragma r:else
	vec3 q = p;
	#pragma r:endif
	planeNormal = normalize(planeNormal);
	q -= planeNormal * THIS_Shift * THIS_DIR;

	#pragma r:if THIS_Direction_custom
	{
		float t = pReflect(q, planeNormal, 0.);
		THIS_exposeSide(ctx, t);
	}
	#pragma r:else
	{
		float q0 = q.THIS_AXIS * THIS_DIR;
		THIS_exposeSide(ctx, sgn(q0));

		float b = THIS_Blend * THIS_Enableblend;
		q0 = sabs(q0, b);

		q.THIS_AXIS = q0 * THIS_DIR;
	}
	#pragma r:endif
	float offset = THIS_Offset;
	q -= planeNormal * offset * THIS_DIR;

	#pragma r:if THIS_COORD_TYPE_vec2
	p = q.xy;
	#pragma r:else
	p = q;
	#pragma r:endif
	ReturnT res;
	#pragma r:if THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#pragma r:else
	res = adaptAsVec4(p);
	#pragma r:endif
	return res;
}
