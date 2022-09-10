ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		ReturnT low = THIS_asReturnT(THIS_Low);
		ReturnT high = THIS_asReturnT(THIS_High);
		BODY();
	}
	return val;
}