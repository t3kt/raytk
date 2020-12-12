ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	pR(q, THIS_Rotate);
	float cell = THIS_EXPR;
	pR(q, THIS_Prerotate);
	p.THIS_PLANE = q - THIS_Offset;
	#ifdef THIS_ITERATE_CELLS
	ctx.iteration.x = cell;
	ctx.iteration.y = THIS_Repetitions;
	#endif
	return inputOp1(p, ctx);
}