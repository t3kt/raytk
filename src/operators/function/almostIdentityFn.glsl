// https://iquilezles.org/www/articles/functions/functions.htm

ReturnT thismap(CoordT p, ContextT ctx) {
	float x = p;
	float m = THIS_Threshold;
	float n = THIS_Basevalue;
	if( x>m ) return x;
	float a = 2.0*n - m;
	float b = 2.0*m - 3.0*n;
	float t = x/m;
	return (a*t + b)*t*t + n;
}