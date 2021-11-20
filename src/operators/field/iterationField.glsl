ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Format_full
	return extractIteration(ctx);
	#pragma r:else
	return extractIteration(ctx).THIS_Format;
	#pragma r:endif
}