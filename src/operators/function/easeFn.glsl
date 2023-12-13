ReturnT thismap(CoordT p, ContextT ctx) {
	float x = p;
	#ifdef THIS_HAS_INPUT_exponentField
	float a = inputOp_exponentField(p, ctx);
	#else
	float a = THIS_Exponent;
	#endif

	const float epsilon = 0.00001;
	const float min_param_a = 0.0 + epsilon;
	const float max_param_a = 1.0 - epsilon;
	a = max(min_param_a, min(max_param_a, a));

	if (a < 0.5)
	{
		// emphasis
		a = 2.0*(a);
		float y = pow(x, a);
		return y;
	} else {
		// de-emphasis
		a = 2.0*(a-0.5);
		float y = pow(x, 1.0/(1-a));
		return y;
	}
}
