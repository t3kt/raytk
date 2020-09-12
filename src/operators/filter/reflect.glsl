ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Planenormal * THIS_Shift;
#ifdef THIS_EXPOSE_ITERATION
	ctx.iteration.x = pReflect(p, THIS_Planenormal, THIS_Offset);
	ctx.iteration.y = 2;
#else
	pReflect(p, THIS_Planenormal, THIS_Offset);
#endif
	return inputOp1(p, ctx);
}
