ReturnT thismap(CoordT p, ContextT ctx) {
	#ifndef THIS_USE_LENGTH
	return inputOp1(p, ctx).THIS_PART;
	#else
	return length(inputOp1(p, ctx).THIS_PARTS);
	#endif
}

