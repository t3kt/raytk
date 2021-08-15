ReturnT thismap(CoordT p, ContextT ctx) {
	float e = THIS_Exponent;
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_1
	r *= inputOp1(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_2
	e *= inputOp2(p, ctx);
	#endif
	p = abs(p);
	return createSdf(pow(pow(p.x,e)+pow(p.y,e),1./e)-r);
}