float thismap(float p, ContextT ctx) {
	float res = THIS_EXPR;
	#ifdef THIS_Invert
	res = 1.0 - res;
	#endif
	return res;
}
