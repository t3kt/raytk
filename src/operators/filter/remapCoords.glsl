ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	CoordT p2 = THIS_asCoordT(inputOp_coordField(p, ctx));
	CoordT q;
	switch (int(THIS_Remapmode)) {
		case THISTYPE_Remapmode_replace: q = p2; break;
		case THISTYPE_Remapmode_add: q = p + p2; break;
		case THISTYPE_Remapmode_multiply: q = p * p2; break;
	}
	q = mix(p, q, THIS_Mix);
	return inputOp1(q, ctx);
}