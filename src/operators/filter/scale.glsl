ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_GET_SCALE();
	ReturnT res = inputOp1(p / scale, ctx);
	#ifdef THIS_RETURN_TYPE_float
	res /= length(scale);
	#else
	res.x /= length(scale);
	#endif
	return res;
}
