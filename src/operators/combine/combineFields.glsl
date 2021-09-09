ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT a = ReturnT(inputOp1(p, ctx));
	ReturnT b = ReturnT(inputOp2(p, ctx));
	if (THIS_Swaporder > 0.) {
		ReturnT tmp = a;
		a = b;
		b = tmp;
	}
	ReturnT res;
	BODY();
	return res;
}