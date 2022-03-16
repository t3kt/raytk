void THIS_apply(inout vec2 p, out float cell) {
	float repetitions = THIS_Repetitions;
	float angle = 2*PI/repetitions;
	float a = atan(p.y, p.x) + angle/2.;
	float r = length(p);
	cell = floor(a/angle);
	#pragma r:if THIS_Uselimit
	{
		float start = THIS_Limitlow;
		float stop = THIS_Limithigh;
		float a2 = mod(a, 2.*PI)/angle;
		if (a2 < start) {
			cell = -1.;
			return;
		}
		if (a2 > stop) {
			cell = repetitions + 1.;
			return;
		}
		#pragma r:if THIS_Mirrortype_mirror
		float a1 = mod(a, angle * 2);
		if (a1 >= angle) {
			a1 = angle - a1;
		}
		a = mod(a1, angle) - angle/2.;
		#pragma r:else
		a = mod(a, angle) - angle/2.;
		#pragma r:endif
	}
	#pragma r:else
  {
		#pragma r:if THIS_Mirrortype_mirror
		// no limit + mirror
		float a1 = mod(a, angle * 2);
		if (a1 >= angle) {
			a1 = angle - a1;
		}
		a = mod(a1, angle) - angle/2.;
		#pragma r:else
		// no limit no mirror
		a = mod(a, angle) - angle/2.;
		#pragma r:endif
	}
	#pragma r:endif
	p = vec2(cos(a), sin(a))*r;
	// For an odd number of repetitions, fix cell index of the cell in -x direction
	// (cell index would be e.g. -5 and 5 in the two halves of the cell):
	if (abs(cell) >= (repetitions/2)) cell = abs(cell);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		vec2 pivot = THIS_Pivot;
		vec2 q = p.THIS_PLANE;
		q -= pivot;
		float r = THIS_Rotate;
		#pragma r:if THIS_HAS_INPUT_rotateField
		r += radians(inputOp_rotateField(p, ctx));
		#pragma r:endif
		pR(q, r);
		float cell;
		THIS_apply(q, cell);
		#pragma r:if THIS_Iterationtype_index
		setIterationIndex(ctx, cell);
		#pragma r:elif THIS_Iterationtype_ratio
		setIterationIndex(ctx, cell / (THIS_Repetitions - 1.));
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_step
		THIS_step = cell;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normstep
		THIS_normstep = cell / (THIS_Repetitions - 1.);
		#pragma r:endif
		float pr = THIS_Prerotate;
		#pragma r:if THIS_HAS_INPUT_preRotateField
		pr += radians(inputOp_preRotateField(p, ctx));
		#pragma r:endif
		pR(q, pr);
		vec2 o = THIS_Offset;
		#pragma r:if THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx).xy;
		#pragma r:endif
		p.THIS_PLANE = q - o + pivot;
	}
	return inputOp1(p, ctx);
}