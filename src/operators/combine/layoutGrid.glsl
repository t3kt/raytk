ReturnT thismap(CoordT p, ContextT ctx) {
	int axis = int(THIS_Axis);
	vec3 scale = THIS_Prescale;
	float scaleMult = vmax(scale);
	ReturnT res;
	#if THIS_INPUT_COUNT == 0
		initDefVal(res);
	#elif THIS_INPUT_COUNT == 1
		p /= scale;
		res = withAdjustedScale(inputOp1(p, ctx), scaleMult);
	#else
	{
		vec2 planePos = getAxisPlane(p, axis);
		#if defined(THIS_ROW)
		float cellSize = THIS_Size.x / float(THIS_INPUT_COUNT);
		float cellPos = planePos.x + THIS_Size.x * 0.25;
		int cell = clamp(int(pModInterval1(cellPos, cellSize, 0, THIS_INPUT_COUNT - 1.)), 0, THIS_INPUT_COUNT - 1);
		setAxisPlanePart1(p, axis, cellPos);
		#elif defined(THIS_COL)
		float cellSize = THIS_Size.y / float(THIS_INPUT_COUNT);
		float cellPos = planePos.y + THIS_Size.y * 0.5;
		int cell = clamp(int(pModInterval1(cellPos, cellSize, 0, THIS_INPUT_COUNT - 1.)), 0, THIS_INPUT_COUNT - 1);
		setAxisPlanePart2(p, axis, cellPos);
		#elif defined(THIS_GRID_ROWS)
		vec2 cellSize = THIS_Size * 0.5;
		int cell;
		if (THIS_INPUT_COUNT == 3 && planePos.y < 0.) {
			cell = 2;
			planePos += cellSize;
		} else {
			cell = quadrantIndex(ivec2(sgn(planePos)) * ivec2(1, -1));
			planePos -= cellSize * sgn(planePos);
		}
		setAxisPlane(p, axis, planePos);
		#else
		#error invalidLayout
		#endif
		p /= THIS_asCoordT(scale);
		if (cell < 1) {
			res = withAdjustedScale(inputOp1(p, ctx), scaleMult);
		} else  if (cell < 2) {
			res = withAdjustedScale(inputOp2(p, ctx), scaleMult);
		}
		#if THIS_INPUT_COUNT > 2
		else if (cell < 3) {
			res = withAdjustedScale(inputOp3(p, ctx), scaleMult);
		} else {
			#if THIS_INPUT_COUNT > 3
			res = withAdjustedScale(inputOp4(p, ctx), scaleMult);
			#else
			res = withAdjustedScale(inputOp3(p, ctx), scaleMult);
			#endif
		}
		#else
		res = withAdjustedScale(inputOp2(p, ctx), scaleMult);
		#endif
	}
	#endif
	return res;
}