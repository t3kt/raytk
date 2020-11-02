float thismap(float p, ContextT ctx) {
	float a = THIS_Balance;
	float b = THIS_Slope;
	#ifdef THIS_NORM
	float k = pow(a+b, a+b) / (pow(a, a)*pow(b, b));
	#else
	float k = THIS_Scale;
	#endif
	return k * pow(p, a) * pow(1.0-p, b);
}