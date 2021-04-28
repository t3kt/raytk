ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 planeNormal = THIS_AXIS_VEC;
	#ifdef THIS_COORD_TYPE_vec2
	vec3 q = vec3(p, 0.);
	planeNormal.z = 0.;
	#else
	vec3 q = p;
	#endif
	planeNormal = normalize(planeNormal);
	q -= planeNormal * THIS_Shift * THIS_DIR;
	float t = dot(q, planeNormal);

	if (t < 0) {
		q = q - (2.*t) * planeNormal;
	}
	float i = sgn(t) * THIS_DIR;
	#if defined(THIS_Iterationtype_sign)
	setIterationIndex(ctx, i);
	#elif defined(THIS_Iterationtype_index)
	//  (-1, 1)  --> (1, 0)
	setIterationIndex(ctx, (i < 0) ? 1: 0);
	#endif
	float offset = THIS_Offset;
	#ifdef THIS_Enableblend
	{
		float b = clamp((abs(t)+offset) / THIS_Blendrange, 0., 1.);
		#ifdef THIS_HAS_INPUT_2
		offset += inputOp2(b, ctx) * THIS_Blendrange;
		#else
		offset += b * THIS_Blendrange;
//		offset += smoothstep(0., 1., b) * THIS_Blendrange;
		#endif
	}
	#endif
	q -= planeNormal * offset * THIS_DIR;
	#ifdef THIS_COORD_TYPE_vec2
	p = q.xy;
	#else
	p = q;
	#endif
	return inputOp1(p, ctx);
}
