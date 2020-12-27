ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
	float radius = THIS_Radius * inputOp3(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	#ifdef THIS_RETURN_TYPE_float
	return fOpPipe(res1, res2, radius);
	#else
	return createSdf(fOpPipe(res1.x, res2.x, radius));
	#endif
}