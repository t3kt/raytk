ReturnT thismap(CoordT p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		return THIS_Multiply;
	#elif THIS_INPUT_COUNT == 1
		return THIS_Multiply * inputOp1(p, ctx);
	#elif THIS_INPUT_COUNT == 2
		return THIS_Multiply * inputOp1(p, ctx) * inputOp2(p, ctx);
	#elif THIS_INPUT_COUNT == 3
		return THIS_Multiply * inputOp1(p, ctx) * inputOp2(p, ctx) * inputOp3(p, ctx);
	#elif THIS_INPUT_COUNT == 4
		return THIS_Multiply * inputOp1(p, ctx) * inputOp2(p, ctx) * inputOp3 * inputOp4(p, ctx);
	#endif
}