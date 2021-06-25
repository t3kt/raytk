ReturnT thismap(vec3 p, ContextT ctx) {
	p.THIS_AXIS -= THIS_Axisoffset;
	vec2 q = vec2(length(p.THIS_PLANE) - THIS_Radialoffset, p.THIS_AXIS);
	float a = atan(p.THIS_PLANE_P2, p.THIS_PLANE_P1) / TAU;
	#ifdef THIS_Iterationtype_ratio
	setIterationIndex(ctx, a);
	#endif
	#ifdef THIS_HAS_INPUT_2
	float r = inputOp2(a, ctx);
	pR(q, radians(r));
	#endif
	float scaleMult = 1.;
	#ifdef THIS_HAS_INPUT_3
	float s = inputOp3(a, ctx);
	q /= s;
	scaleMult = s;
	#endif
	#ifdef THIS_HAS_INPUT_4
		q -= inputOp4(a, ctx).xy;
	#endif
	return withAdjustedScale(inputOp1(q, ctx), scaleMult);
}