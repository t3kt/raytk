ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res1 = inputOp1(p, ctx);
	Sdf res2 = inputOp2(p, ctx);
	if (THIS_Swaporder > 0.) {
		swap(res1, res2);
	}
	return cmb_simpleDiff(res1, res2);
}