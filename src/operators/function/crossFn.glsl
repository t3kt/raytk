ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), inputOp3(p, ctx));
	#else
	return mix(inputOp1(p, ctx), inputOp2(p, ctx), THIS_Mix);
	#endif
}