ReturnT thismap(CoordT p, ContextT ctx) {
	float q = p.THIS_AXIS + THIS_Shift;
	#ifdef THIS_Uselimit
	float cell = THIS_FUNC(q, THIS_Size, THIS_Limitstart, THIS_Limitstop);
	#else
	float cell = THIS_FUNC(q, THIS_Size);
	#endif
	p.THIS_AXIS = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationIndex(ctx, cell);
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationIndex(ctx, mod(cell, 2.));
	#endif
	return inputOp1(p, ctx);
}