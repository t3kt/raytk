ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 planeNormal = THIS_AXIS_VEC;
	p -= planeNormal * THIS_Shift * THIS_DIR;
	float t = dot(p, planeNormal) + THIS_Offset * THIS_DIR;

#ifdef THIS_HAS_INPUT_2
	t = sgn(t) * inputOp2(abs(t), ctx);
#endif

	if (t < 0) {
		p = p - (2.*t) * planeNormal;
	}
	float i = sgn(t) * THIS_DIR;
#ifdef THIS_Exposeiteration
	ctx.iteration.x = (i + 1.) * .5;
	ctx.iteration.y = 2;
#endif
	return inputOp1(p, ctx);
}
