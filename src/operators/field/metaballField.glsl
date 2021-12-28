ReturnT thismap(CoordT p, ContextT ctx) {
	float d = length(pow(abs(p - THIS_asCoordT(THIS_Center)), THIS_asCoordT(THIS_Exponent)) / (THIS_asCoordT(THIS_Radius) * THIS_Radiusscale));
	return 1 / (d*d) * THIS_Weight;
}