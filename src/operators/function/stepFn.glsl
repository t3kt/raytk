ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifdef THIS_Function_smoothstep
	float low = THIS_Edge - THIS_Blend * 0.5;
	float high = THIS_Edge + THIS_Blend * 0.5;
	res = THIS_Function(low, high, p);
	#else
	res = THIS_Function(THIS_Edge, p);
	#endif
	#ifdef THIS_Invert
	res = 1.0 - res;
	#endif
	return res;
}
