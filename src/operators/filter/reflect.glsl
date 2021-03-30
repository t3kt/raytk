ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 planeNormal = normalize(THIS_AXIS_VEC);
	p -= planeNormal * THIS_Shift * THIS_DIR;
	float t = dot(p, planeNormal);

	if (t < 0) {
		p = p - (2.*t) * planeNormal;
	}
	float i = sgn(t) * THIS_DIR;
	#if defined(THIS_Iterationtype_sign)
	setIterationIndex(ctx, i);
	#elif defined(THIS_Iterationtype_index)
	//  (-1, 1)  --> (1, 0)
	setIterationIndex(ctx, (i < 0) ? 1: 0);
	#endif
	p -= planeNormal * THIS_Offset * THIS_DIR;
	return inputOp1(p, ctx);
}
