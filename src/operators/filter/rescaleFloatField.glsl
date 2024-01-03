ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		res = mapRange(res,
			ReturnT(THIS_Inputrange1), ReturnT(THIS_Inputrange2),
			ReturnT(THIS_Outputrange1), ReturnT(THIS_Outputrange2));
		res *= ReturnT(THIS_Multiply);
		res += ReturnT(THIS_Postadd);
	}
	return res;
}