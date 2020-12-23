ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Mode_index)
	return ctx.iteration.x;
	#elif defined(THIS_Mode_scaledindex)
	if (ctx.iteration.y != 0.) {
		return ctx.iteration.x / ctx.iteration.y;
	} else {
		return ctx.iteration.x;
	}
	#elif defined(THIS_Mode_full)
	return ctx.iteration;
	#endif
}