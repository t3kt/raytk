ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res1 = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable)) { return res1; }
	Sdf res2 = inputOp2(p, ctx);
	if (IS_TRUE(THIS_Swaporder)) {
		swap(res1, res2);
	}
	return cmb_simpleDiff(res1, res2);
}