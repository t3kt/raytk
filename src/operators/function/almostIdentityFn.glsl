// https://iquilezles.org/www/articles/functions/functions.htm

ReturnT thismap(CoordT p, ContextT ctx) {
	float x = p;
	#ifdef THIS_HAS_INPUT_thresholdField
	float m = inputOp_thresholdField(p, ctx);
	#else
	float m = THIS_Threshold;
	#endif
	#ifdef THIS_HAS_INPUT_baseValueField
	float n = inputOp_baseValueField(p, ctx);
	#else
	float n = THIS_Basevalue;
	#endif
	if( x>m ) return x;
	float a = 2.0*n - m;
	float b = 2.0*m - 3.0*n;
	float t = x/m;
	return (a*t + b)*t*t + n;
}