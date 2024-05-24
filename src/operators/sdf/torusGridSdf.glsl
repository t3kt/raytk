void THIS_combine(inout Sdf res1, inout Sdf res2, in CoordT p, in ContextT ctx) {
	MERGE_PREP();
	MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p0 = p;

	// Convert to XZ plane expected by fTorus()
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: p = p.yxz; break;
		case THISTYPE_Axis_y: p = p.xyz; break;
		case THISTYPE_Axis_z: p = p.xzy; break;
	}

	#ifdef THIS_EXPOSE_angle
	THIS_angle = degrees(atan(p.x, p.z)) + 180.;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(p.x, p.z)/TAU + .5;
	#endif

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

	vec2 shift = THIS_Shift;
	#ifdef THIS_HAS_INPUT_shiftField
	shift += fillToVec2(inputOp_shiftField(p0, ctx));
	#endif

	float col;
	float row;
	vec3 pCol;
	vec2 qRow;
	float thCol;
	float thRow;

	int parts = int(THIS_Parts);

	float dCols;
	if (parts == THISTYPE_Parts_both || parts == THISTYPE_Parts_cols) {
		pR(p.xz, shift.x * TAU);
		pCol = p;
		col = pModPolar(pCol.xz, cols);
		#ifdef THIS_EXPOSE_col
		THIS_col = int(col);
		#endif
		#ifdef THIS_EXPOSE_normcol
		THIS_normcol = col / (cols-1.);
		#endif
		pCol.x -= rOuter;
	}

	float dRows;
	if (parts == THISTYPE_Parts_both || parts == THISTYPE_Parts_rows) {
		qRow = vec2(length(p.xz) - rOuter, p.y);
		pR(qRow, shift.y * TAU);
		row = pModPolar(qRow, rows);
		#ifdef THIS_EXPOSE_row
		THIS_row = int(row);
		#endif
		#ifdef THIS_EXPOSE_normrow
		THIS_normrow = row/ (rows-1.);
		#endif
		qRow.x -= thOuter;
	}

	if (parts == THISTYPE_Parts_both || parts == THISTYPE_Parts_cols) {
		#ifdef THIS_HAS_INPUT_barThicknessField
    	thCol = inputOp_barThicknessField(p0, ctx);
		#else
    	thCol = THIS_Barthickness;
		#endif
		dCols = fTorus(pCol.xzy, thCol, thOuter);
	}

	if (parts == THISTYPE_Parts_both || parts == THISTYPE_Parts_rows) {
		#ifdef THIS_HAS_INPUT_barThicknessField
    	thRow = inputOp_barThicknessField(p0, ctx);
		#else
    	thRow = THIS_Barthickness;
		#endif
    	dRows = length(qRow) - thRow;
	}

	Sdf res1;
	switch (parts) {
		case THISTYPE_Parts_both:
			res1 = createSdf(dRows);
			Sdf res2 = createSdf(dCols);
			THIS_combine(res1, res2, p0, ctx);
			break;
		case THISTYPE_Parts_cols:
			res1 = createSdf(dCols);
			break;
		case THISTYPE_Parts_rows:
			res1 = createSdf(dRows);
			break;
	}

	return res1;
}