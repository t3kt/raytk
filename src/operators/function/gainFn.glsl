ReturnT thismap(CoordT p, ContextT ctx) {
	float k = THIS_Exponent;
	float a = 0.5*pow(2.0*((p<0.5)?p:1.0-p), k);
	return (p<0.5)?a:1.0-a;
}