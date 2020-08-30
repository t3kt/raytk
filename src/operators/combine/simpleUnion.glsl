ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	return res1.x < res2.x ? res1 : res2;
	#else
	return min(res1, res2);
	#endif
}