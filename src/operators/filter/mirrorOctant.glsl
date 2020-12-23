ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	vec2 cell = pMirrorOctant(q, THIS_Size);
	pR(q, THIS_Rotateaxis);
	p.THIS_PLANE = q - THIS_Offset;
	#ifdef THIS_Iterateoncells
	ctx.iteration.x = quadrantIndex(ivec2(cell));
	ctx.iteration.y = 4;
	#endif
	return inputOp1(p, ctx);
}