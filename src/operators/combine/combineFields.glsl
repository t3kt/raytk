ReturnT THIS_combine(ReturnT a, ReturnT b) {
	ReturnT res;
	if (IS_TRUE(THIS_Swaporder)) {
		ReturnT tmp = a;
		a = b;
		b = tmp;
	}
	BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT a = ReturnT(inputOp1(p, ctx));
	if (IS_FALSE(THIS_Enable)) { return a; }
	ReturnT res;
	AGGREGATE_BODY();
	return res;
}