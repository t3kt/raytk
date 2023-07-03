void THIS_apply(inout vec2 p, out float cell) {
	float repetitions = THIS_Repetitions;
	float angle = TAU/repetitions;
	float a = atan(p.y, p.x) + angle/2.;
	cell = floor(a/angle);
	if (THIS_Uselimit) {
		float start = THIS_Limitlow;
		float stop = THIS_Limithigh;
		float a2 = mod(a, TAU)/angle;
		if (a2 < start) {
			cell = -1.;
			return;
		}
		if (a2 > stop) {
			cell = repetitions + 1.;
			return;
		}
		if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
			float a1 = mod(a, angle * 2);
			if (a1 >= angle) {
				a1 = angle - a1;
			}
			a = mod(a1, angle) - angle/2.;
		} else {
			a = mod(a, angle) - angle/2.;
		}
	} else {
		if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
			// no limit + mirror
			float a1 = mod(a, angle * 2);
			if (a1 >= angle) {
				a1 = angle - a1;
			}
			a = mod(a1, angle) - angle/2.;
		} else {
			// no limit no mirror
			a = mod(a, angle) - angle/2.;
		}
	}
	#ifdef THIS_EXPOSE_normlocalangle
	THIS_normlocalangle = a + .5;
	#endif
	p = vec2(cos(a), sin(a))*length(p);
	// For an odd number of repetitions, fix cell index of the cell in -x direction
	// (cell index would be e.g. -5 and 5 in the two halves of the cell):
	if (abs(cell) >= (repetitions/2)) cell = abs(cell);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec2 pivot = THIS_Pivot;
		vec2 q;
		switch (int(THIS_Axis)) {
			case THISTYPE_Axis_x: q = p3.zy; break;
			case THISTYPE_Axis_y: q = p3.zx; break;
			case THISTYPE_Axis_z: q = p3.xy; break;
		}
		q -= pivot;
		#ifdef THIS_EXPOSE_centerdist
		THIS_centerdist = length(q);
		#endif
		float r = THIS_Rotate - radians(90.0);
		#ifdef THIS_HAS_INPUT_rotateField
		r += radians(inputOp_rotateField(p, ctx));
		#endif
		pR(q, r);
		float globalAngle = atan(q.y, q.x) / TAU;
		#ifdef THIS_EXPOSE_globalangle
		THIS_globalangle = globalAngle * 360.;
		#endif
		#ifdef THIS_EXPOSE_normglobalangle
		THIS_normglobalangle = globalAngle + .5;
		#endif
		float cell;
		THIS_apply(q, cell);
		switch (THIS_Iterationtype) {
			case THISTYPE_Iterationtype_index:
				setIterationIndex(ctx, cell);
				break;
			case THISTYPE_Iterationtype_ratio:
				setIterationIndex(ctx, cell / (THIS_Repetitions - 1.));
				break;
		}
		#ifdef THIS_EXPOSE_step
		THIS_step = cell;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = cell / (THIS_Repetitions - 1.);
		#endif
		float pr = THIS_Prerotate;
		#ifdef THIS_HAS_INPUT_preRotateField
		pr += radians(inputOp_preRotateField(p, ctx));
		#endif
		pR(q, pr);
		vec2 o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx).xy;
		#endif
		q = q - o + pivot;
		switch (int(THIS_Axis)) {
			case THISTYPE_Axis_x: p3.zy = q; break;
			case THISTYPE_Axis_y: p3.zx = q; break;
			case THISTYPE_Axis_z: p3.xy = q; break;
		}
		p = THIS_asCoordT(p3);
	}
	return inputOp1(p, ctx);
}