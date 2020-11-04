ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_USE_MIX_FIELD
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), inputOp3(p, ctx));
	#else
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), THIS_Mix);
	#endif
}