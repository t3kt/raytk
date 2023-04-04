ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q;
	float z;
	BODY();
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = z;
	#endif
	return inputOp1(q, ctx);
}