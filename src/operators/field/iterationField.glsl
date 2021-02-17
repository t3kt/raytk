ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Format_full)
	return ctx.iteration;
	#else
	return ctx.iteration.THIS_Format;
	#endif
}