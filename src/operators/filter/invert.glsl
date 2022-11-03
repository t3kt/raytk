ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		#ifdef THIS_RETURN_TYPE_Sdf
		res.x *= -1;
		#else
		res *= -1.;
		#endif
	}
	return res;
}
