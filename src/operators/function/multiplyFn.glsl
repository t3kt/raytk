ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = ReturnT(THIS_Multiply);
	#ifdef THIS_HAS_INPUT_1
	res *= inputOp1(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_2
	res *= inputOp2(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_3
	res *= inputOp3(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_4
	res *= inputOp4(p, ctx);
	#endif
	return res;
}