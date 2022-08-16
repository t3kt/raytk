ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = fillToVec4(inputOp1(p, ctx));
	if (IS_FALSE(THIS_Enable)) { return res1; }
	ReturnT res2 = fillToVec4(inputOp2(p, ctx));
	if (IS_TRUE(THIS_Swapinputs)) {
		swap(res1, res2);
	}
	float amt = THIS_Blend;
	ReturnT res;
	BODY();
	return res;
}