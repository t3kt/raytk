ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE + THIS_Shift;
	vec2 cell = THIS_MIRROR_FUNC(q, THIS_Size);
	p.THIS_PLANE = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationIndex(ctx, cell);
	#elif defined(THIS_Iterationtype_tiledquadrant)
	setIterationIndex(ctx, quadrantIndex(mod(ivec2(cell), 2)));
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationCell(ctx, mod(cell, 2.));
	#endif
	return inputOp1(p, ctx);
}