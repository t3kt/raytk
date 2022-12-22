ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p0;
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: p0 = p.zyx; break;
		case THISTYPE_Axis_y: p0 = p.xzy; break;
		case THISTYPE_Axis_z: p0 = p; break;
	}
	vec2 q = vec2(length(p0.xy) - THIS_Radialoffset, p0.z - THIS_Axisoffset);
	float a = atan(p0.y, p0.x) / TAU;
	if (THIS_Iterationtype == THISTYPE_Iterationtype_ratio) {
		setIterationIndex(ctx, a);
	}
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = .5 + a*.5;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = 360. * a;
	#endif
	#ifdef THIS_HAS_INPUT_rotateField
	#ifdef inputOp_rotateField_COORD_TYPE_float
	float r = inputOp_rotateField(a, ctx);
	#else
	float r = inputOp_rotateField(p, ctx);
	#endif
	pR(q, radians(r));
	#endif
	float scaleMult = 1.;
	#ifdef THIS_HAS_INPUT_scaleField
	#ifdef inputOp_scaleField_COORD_TYPE_float
	float s = inputOp_scaleField(a, ctx);
	#else
	float s = inputOp_scaleField(p, ctx);
	#endif
	q /= s;
	scaleMult = s;
	#endif
	#ifdef inputOp_translateField_COORD_TYPE_float
		q -= inputOp_translateField(a, ctx).xy;
	#elif defined(THIS_HAS_INPUT_translateField_COORD_TYPE_vec3)
		q -= fillToVec2(inputOp_translateField(p, ctx));
	#endif
	return withAdjustedScale(inputOp_crossSection(q, ctx), scaleMult);
}