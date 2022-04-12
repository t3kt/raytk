ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return THIS_INPUT_1(p, ctx);
	}
	BODY();
	return res;
}