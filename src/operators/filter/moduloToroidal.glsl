ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	vec3 p0 = p;

	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x:
			p = p.zxy;
			break;
		case THISTYPE_Axis_y:
			p = p.xyz;
			break;
		case THISTYPE_Axis_z:
			p = p.xzy;
			break;
	}

	#ifdef THIS_HAS_INPUT_radiusField
	float rOuter = inputOp_radiusField(p0, ctx);
	#else
	float rOuter = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float thOuter = inputOp_thicknessField(p0, ctx);
	#else
	float thOuter = THIS_Thickness;
	#endif

	#ifdef THIS_HAS_INPUT_repetitionsField
	vec2 r = fillToVec2(inputOp_repetitionsField(p0, ctx));
	#else
	vec2 r = THIS_Repetitions;
	#endif

	vec2 shift = THIS_Shift;

	#ifdef THIS_HAS_INPUT_shiftField
	shift += fillToVec2(inputOp_shiftField(p0, ctx));
	#endif

	shift *= TAU;

	float col;
	float row;

	pR(p.xz, shift.y);
	col = pModPolar(p.xz, r.x);
	p.x -= rOuter;

	pR(p.xy, shift.x);
	row = pModPolar(p.xy, r.y);
	p.x -= thOuter;

	#ifdef THIS_EXPOSE_cell
	THIS_cell = vec2(col, row);
	#endif

	#ifdef THIS_EXPOSE_normcell
	THIS_normcell = vec2(col, row) / r;
	#endif

	return inputOp1(p.yxz, ctx);
}