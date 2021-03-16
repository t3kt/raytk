ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p + THIS_Shift;
	vec3 cell = pMod3(q, THIS_Size);
	p = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationCell(ctx, cell);
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationCell(ctx, mod(cell, 2.));
	#endif
	return inputOp1(p, ctx);
}