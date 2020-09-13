ReturnT thismap(CoordT p, ContextT ctx) {
	float q = p.THIS_AXIS + THIS_Shift;
	float cell = THIS_MIRROR_FUNC(q, THIS_Size);
	p.THIS_AXIS = q - THIS_Offset;
	#ifdef THIS_ITERATE_CELLS
	ctx.iteration.x = clamp(cell, 0, 1);
	ctx.iteration.y = 2;
	#endif
	return inputOp1(p, ctx);
}