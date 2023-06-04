ReturnT thismap(CoordT p, ContextT ctx) {
	float res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		res = mapRange(res, THIS_Inputrange1, THIS_Inputrange2, THIS_Outputrange1, THIS_Outputrange2);
		res *= THIS_Multiply;
		res += THIS_Postadd;
	}
	return res;
}