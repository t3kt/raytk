ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res.x -= THIS_GET_AMOUNT();
	#else
	res -= THIS_GET_AMOUNT();
	#endif
	return res;
}