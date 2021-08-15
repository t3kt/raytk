ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = mapRange(inputOp1(p, ctx),
		THIS_asReturnT(THIS_Inputlow), THIS_asReturnT(THIS_Inputhigh),
		THIS_asReturnT(THIS_Outputlow), THIS_asReturnT(THIS_Outputhigh));
	res *= THIS_Multiply * THIS_asReturnT(THIS_Mult);
	return res + THIS_asReturnT(THIS_Postadd);
}