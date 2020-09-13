ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_AXIS_PLANE + THIS_Shift;
	vec2 cell = THIS_MIRROR_FUNC(q, THIS_Size);
	p.THIS_AXIS_PLANE = q - THIS_Offset;
	#ifdef THIS_ITERATE_CELLS
	ctx.iteration.x = quadrantIndex(ivec2(cell));
	ctx.iteration.y = 4;
	#endif
	return inputOp1(p, ctx);
}