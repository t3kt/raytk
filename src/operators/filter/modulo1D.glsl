ReturnT thismap(CoordT p, ContextT ctx) {
	float q = p.THIS_AXIS + THIS_Shift;
	#ifdef THIS_Uselimit
	float cell = THIS_FUNC(q, THIS_Size, THIS_Limitstart, THIS_Limitstop);
	#else
	float cell = THIS_FUNC(q, THIS_Size);
	#endif
	p.THIS_AXIS = q - THIS_Offset;
	#ifdef THIS_Iterateoncells
	ctx.iteration.x = cell;
	ctx.iteration.y = 2;
	#endif
	return inputOp1(p, ctx);
}