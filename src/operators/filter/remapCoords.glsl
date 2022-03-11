ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable < 0.5) { return inputOp1(p, ctx); }
	CoordT p2 = THIS_asCoordT(inputOp_coordField(p, ctx));
	#pragma r:if THIS_Remapmode_replace
	CoordT q = p2;
	#pragma r:elif THIS_Remapmode_add
	CoordT q = p + p2;
	#pragma r:elif THIS_Remapmode_multiply
	CoordT q = p * p2;
	#pragma r:else
	#error invalidRemapMode
	#pragma r:endif
	q = mix(p, q, THIS_Mix);
	return inputOp1(q, ctx);
}