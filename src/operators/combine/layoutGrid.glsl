ReturnT thismap(CoordT p, ContextT ctx) {
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
		#if defined(THIS_ROW)
		float cellSize = THIS_Size1 / float(THIS_INPUT_COUNT);
		float cellPos = p.THIS_PLANE_P1 + THIS_Size1 * 0.25;
		int cell = clamp(int(pModInterval1(cellPos, cellSize, 0, THIS_INPUT_COUNT - 1.)), 0, THIS_INPUT_COUNT - 1);
		p.THIS_PLANE_P1 = cellPos;
		#elif defined(THIS_COL)
		float cellSize = THIS_Size2 / float(THIS_INPUT_COUNT);
		float cellPos = p.THIS_PLANE_P2 + THIS_Size2 * 0.5;
		int cell = clamp(int(pModInterval1(cellPos, cellSize, 0, THIS_INPUT_COUNT - 1.)), 0, THIS_INPUT_COUNT - 1);
		p.THIS_PLANE_P2 = cellPos;
		#elif defined(THIS_GRID_ROWS)
		vec2 cellSize = THIS_Size * 0.5;
		int cell;
		if (THIS_INPUT_COUNT == 3 && p.THIS_PLANE_P2 < 0.) {
			cell = 2;
			p.THIS_PLANE += cellSize;
		} else {
			cell = quadrantIndex(ivec2(sgn(p.THIS_PLANE)) * ivec2(1, -1));
			p.THIS_PLANE -= cellSize * sgn(p.THIS_PLANE);
		}
		#else
		#error invalidLayout
		#endif
		p /= scale;
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