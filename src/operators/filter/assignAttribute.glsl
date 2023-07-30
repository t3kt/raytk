ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable)) { return res; }
	#ifdef THIS_EXPOSE_sdf
	THIS_sdf = res;
	#endif
	#ifdef THIS_ATTR_EXISTS
	{
		#ifdef THIS_EXPOSE_previous
		THIS_previous = res.attrs.THIS_NAME;
		#endif
		#ifdef THIS_HAS_INPUT_valueField
		res.attrs.THIS_NAME = inputOp_valueField(p, ctx);
		#else
		res.attrs.THIS_NAME = THIS_asValueT(THIS_Value);
		#endif
	}
	#endif
	return res;
}