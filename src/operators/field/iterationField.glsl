ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 val = extractIteration(ctx);
	#if defined(THIS_Format_full)
	return val;
	#else
	return val.THIS_Format;
	#endif
}