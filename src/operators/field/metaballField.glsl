float thismap(CoordT p, ContextT ctx) {
#ifdef THIS_COORD_TYPE_float
	float d = abs(pow(abs(p - THIS_Centerx), THIS_Exponentx) / THIS_Radiusx);
#else
	float d = length(pow(abs(p - THIS_Center), THIS_Exponent) / THIS_Radius);
#endif
	float amt = 1 / (d*d);
	return amt * THIS_Weight;
}