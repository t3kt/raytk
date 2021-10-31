ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_USE_LENGTH
	return length(inputOp1(p, ctx).THIS_PARTS);
	#pragma r:else
	return inputOp1(p, ctx).THIS_PART;
	#pragma r:endif
}

