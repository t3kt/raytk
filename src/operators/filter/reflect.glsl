ReturnT thismap(CoordT p, ContextT ctx) {
#ifdef THIS_CUSTOM
	p -= THIS_Planenormal * THIS_Shift;
	vec3 planeNormal = THIS_Planenormal;
	float t = dot(p, planeNormal)+THIS_Offset;

	#ifdef THIS_USE_BLEND_FUNC
	t = sgn(t) * inputOp2(abs(t), ctx);
	#endif

	if (t < 0) {
		p = p - (2.*t) * planeNormal;
	}
	float i = sgn(t);
#else
	float q = abs(p.THIS_AXIS - THIS_Shift);
	#ifdef THIS_USE_BLEND_FUNC
	if (q <= 1.) {
		q = inputOp2(q, ctx);
	}
//	q *= inputOp2(q, ctx);
	#endif
	p.THIS_AXIS = q;
#endif
#ifdef THIS_EXPOSE_ITERATION
	ctx.iteration.x = (i + 1.) * .5;
	ctx.iteration.y = 2;
#endif
	return inputOp1(p, ctx);
}
