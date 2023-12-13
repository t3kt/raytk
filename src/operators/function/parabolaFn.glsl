ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_exponentField
	float k = inputOp_exponentField(p, ctx);
	#else
	float k = THIS_Exponent;
	#endif
	return pow(4.0*p*(1.0-p), k);
}