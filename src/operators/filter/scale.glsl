ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p / THIS_Scale, ctx);
	#ifdef THIS_RETURN_TYPE_float
	res /= length(THIS_Scale);
	#else
	res.x /= length(THIS_Scale);
	#endif
	return res;
}
