ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	vec3 p0 = p;

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

	float rows = THIS_Rows;
	float cols = THIS_Cols;

	float col;
	float row;

	col = pModPolar(p.xz, cols);
	p.x -= rOuter;

	row = pModPolar(p.xy, rows);
	p.x -= thOuter;

	#ifdef THIS_EXPOSE_cell
	THIS_cell = vec2(col, row);
	#endif

	#ifdef THIS_EXPOSE_normcell
	THIS_normcell = vec2(col, row) / vec2(cols, rows);
	#endif

	return inputOp1(p, ctx);
}