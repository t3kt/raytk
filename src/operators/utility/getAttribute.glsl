ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifndef THIS_HAS_ATTR
	res = ReturnT(0.);
	#else
	{
		Sdf sdf;
		#ifdef THIS_HAS_INPUT_sdf
		sdf = inputOp_sdf(p, ctx);
		#else
		sdf = ctx.result;
		#endif
		res = sdf.attrs.THIS_NAME;
	}
	#endif
	return res;
}