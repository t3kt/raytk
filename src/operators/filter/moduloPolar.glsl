ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	pR(q, THIS_Rotate);
	float cell = THIS_MIRROR_FUNC(q, THIS_Repetitions);
	pR(q, THIS_Prerotate);
	p.THIS_PLANE = q - THIS_Offset;
	#ifdef THIS_ITERATE_CELLS
	ctx.iteration.x = clamp(cell, 0, 1);
	ctx.iteration.y = 2;
	#endif
	return inputOp1(p, ctx);
}