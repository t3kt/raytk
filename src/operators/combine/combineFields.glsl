ReturnT thismap(CoordT p, ContextT ctx) {
	return THIS_COMBINE(THIS_INPUT_OP_1(p, ctx), THIS_INPUT_OP_2(p, ctx));
}