ReturnT thismap(CoordT p, ContextT ctx) {
#ifdef THIS_RETURN_TYPE_Sdf
	ReturnT res = inputOp1(p, ctx);
	res.x = onion(res.x, THIS_Thickness);
	return res;
#else
	return onion(inputOp1(p, ctx), THIS_Thickness);
#endif
}