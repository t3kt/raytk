ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_mixField
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), inputOp_mixField(p, ctx));
	#else
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), THIS_Mix);
	#endif
}