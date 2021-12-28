ReturnT thismap(CoordT p, ContextT ctx) {
	p.THIS_AXIS -= THIS_Axisoffset;
	vec2 q = vec2(length(p.THIS_PLANE) - THIS_Radialoffset, p.THIS_AXIS);
	float a = atan(p.THIS_PLANE_P2, p.THIS_PLANE_P1) / TAU;
	#pragma r:if THIS_Iterationtype_ratio
	setIterationIndex(ctx, a);
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normangle
	THIS_normangle = .5 + a*.5;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_angle
	THIS_angle = 360. * a;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_rotateField
	float r = inputOp_rotateField(a, ctx);
	pR(q, radians(r));
	#pragma r:endif
	float scaleMult = 1.;
	#pragma r:if THIS_HAS_INPUT_scaleField
	float s = inputOp_scaleField(a, ctx);
	q /= s;
	scaleMult = s;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_translateField
		q -= inputOp_translateField(a, ctx).xy;
	#pragma r:endif
	return withAdjustedScale(inputOp_crossSection(q, ctx), scaleMult);
}