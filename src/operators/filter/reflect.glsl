ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Planenormal * THIS_Shift;
	float i = pReflect(p, THIS_Planenormal, THIS_Offset);
#ifdef THIS_EXPOSE_ITERATION
	ctx.iteration.x = (i + 1.) * .5;
	ctx.iteration.y = 2;
#endif
	return inputOp1(p, ctx);
}
