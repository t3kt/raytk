ReturnT thismap(CoordT p, ContextT ctx) {
	float o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += inputOp_offsetField(p, ctx);
	#endif
	float d;
	BODY();
	return createSdf(d);
}