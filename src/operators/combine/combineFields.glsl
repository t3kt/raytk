ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT a = ReturnT(inputOp1(p, ctx));
	if (IS_FALSE(THIS_Enable)) { return a; }
	ReturnT b = ReturnT(inputOp2(p, ctx));
	if (IS_TRUE(THIS_Swaporder)) {
		ReturnT tmp = a;
		a = b;
		b = tmp;
	}
	ReturnT res;
	BODY();
	return res;
}