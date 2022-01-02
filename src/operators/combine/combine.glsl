void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	#pragma r:if THIS_HAS_INPUT_2
	ReturnT res2 = inputOp2(p, ctx);
	THIS_combine(res1, res2, p, ctx);
	#pragma r:endif
	return res1;
}