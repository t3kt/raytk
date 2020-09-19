#ifdef THIS_RETURN_TYPE_Sdf
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	res.x *= -1;
	return res;
}
#else
#define thismap(p, ctx) -inputOp1(p, ctx)
#endif