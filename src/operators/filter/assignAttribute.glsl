ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable)) { return res; }
	#ifdef THIS_EXPOSE_sdf
	THIS_sdf = res;
	#endif
	#ifdef THIS_ATTR_EXISTS
	res.attrs.THIS_NAME = inputOp_valueField(p, ctx);
	#endif
	return res;
}