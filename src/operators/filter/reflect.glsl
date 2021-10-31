ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 planeNormal = THIS_AXIS_VEC;
	#pragma r:if THIS_COORD_TYPE_vec2
	vec3 q = vec3(p, 0.);
	planeNormal.z = 0.;
	#pragma r:else
	vec3 q = p;
	#pragma r:endif
	planeNormal = normalize(planeNormal);
	q -= planeNormal * THIS_Shift * THIS_DIR;
	float t = dot(q, planeNormal);

	if (t < 0) {
		q = q - (2.*t) * planeNormal;
	}
	float i = sgn(t) * THIS_DIR;
	#pragma r:if THIS_Iterationtype_sign
	setIterationIndex(ctx, i);
	#pragma r:elif THIS_Iterationtype_index
	//  (-1, 1)  --> (1, 0)
	setIterationIndex(ctx, (i < 0) ? 1: 0);
	#pragma r:endif
	float offset = THIS_Offset;
	#pragma r:if THIS_Enableblend
	{
		float b = clamp((abs(t)+offset) / THIS_Blendrange, 0., 1.);
		#pragma r:if THIS_HAS_INPUT_blending
		offset += inputOp_blending(b, ctx) * THIS_Blendrange;
		#pragma r:else
		offset += b * THIS_Blendrange;
//		offset += smoothstep(0., 1., b) * THIS_Blendrange;
		#pragma r:endif
	}
	#pragma r:endif
	q -= planeNormal * offset * THIS_DIR;
	#pragma r:if THIS_COORD_TYPE_vec2
	p = q.xy;
	#pragma r:else
	p = q;
	#pragma r:endif
	return inputOp1(p, ctx);
}
