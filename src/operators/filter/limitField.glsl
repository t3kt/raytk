ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	if (THIS_Enable >= 0.5) {
		ReturnT low = THIS_asReturnT(THIS_Low);
		ReturnT high = THIS_asReturnT(THIS_High);
		BODY();
	}
	return val;
}