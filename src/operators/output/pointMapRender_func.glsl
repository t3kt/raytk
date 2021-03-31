ReturnT thismap(CoordT p, Context ctx) {
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return createNonHitSdf();
	#endif
}