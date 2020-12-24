ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Timesource_global)
	Time time = getGlobalTime();
	#elif defined(THIS_Timesource_context)
	Time time = contextTime(ctx);
	#else
	#error invalidTimeSource
	#endif
	return THIS_EXPR;
}