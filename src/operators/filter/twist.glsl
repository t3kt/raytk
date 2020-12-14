ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p.THIS_PLANE, p.THIS_AXIS * THIS_Amount + THIS_Shift);
	return inputOp1(p, ctx);
}