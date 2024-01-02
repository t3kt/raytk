void THIS_prepareCircle(inout vec3 p0, float space, float shift, out float cell) {
	p0.xy = vec2(length(p0.xy), p0.z);
	p0.x -= (shift+.5) * space;
	cell = pMod1(p0.x, space);
}

void THIS_prepareDiamond(inout vec3 p0, float space, float shift, out float cell) {
	pMirror(p0.x, 0.);
	pMirror(p0.y, 0.);
	pR(p0.xy, radians(-45));
	p0.y -= (shift+.5) * space;
	cell = pMod1(p0.y, space);
	p0 = p0.yzx;
}

void THIS_prepareSquare(inout vec3 p0, float space, float shift, out float cell) {
	pR(p0.xy, radians(-45));
	THIS_prepareDiamond(p0, space, shift, cell);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p0;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: p0 = p.yzx; break;
		case THISTYPE_Axis_y: p0 = p.zxy; break;
		case THISTYPE_Axis_z: p0 = p.xyz; break;
	}
	float a = atan(p0.y, p0.x) / TAU;
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = .5 + a*.5;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = 360. * a;
	#endif
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = p0.z;
	#endif
	#ifdef THIS_HAS_INPUT_spacingField
	float space = inputOp_spacingField(p, ctx);
	#else
	float space = THIS_Spacing;
	#endif
	#ifdef THIS_HAS_INPUT_shiftField
	float shift = inputOp_shiftField(p, ctx);
	#else
	float shift = THIS_Shift;
	#endif
	float cell;
	BODY();
	#ifdef THIS_EXPOSE_ring
	THIS_ring = int(cell);
	#endif
	vec2 q = p0.xy;
	Sdf res;
	#ifdef THIS_HAS_INPUT_crossSection
	res = inputOp_crossSection(q, ctx);
	#else
	#ifdef THIS_HAS_INPUT_thicknessField
	float thickness = inputOp_thicknessField(p, ctx);
	#else
	float thickness = THIS_Thickness;
	#endif
	res = createSdf(length(q) - thickness);
	#endif
	return res;
}