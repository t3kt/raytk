ReturnT thismap(CoordT p, ContextT ctx) {
	float e = THIS_Exponent;
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_exponentField
	e *= inputOp_exponentField(p, ctx);
	#endif
	p = abs(p);
	return createSdf(pow(pow(p.x,e)+pow(p.y,e),1./e)-r);
}