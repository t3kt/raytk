ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	pR(q, THIS_Rotate);
	float cell = THIS_EXPR;
	pR(q, THIS_Prerotate);
	p.THIS_PLANE = q - THIS_Offset;
	#ifdef THIS_Iterateoncells
	setIterationIndex(ctx, cell);
	#endif
	return inputOp1(p, ctx);
}