ReturnT thismap(CoordT p, ContextT ctx) {
	float d1 = length(p - THIS_Point1);
	float d2 = length(p - THIS_Point2);
	float d3 = length(p - THIS_Point3);
	float d4 = length(p - THIS_Point4);

	ReturnT v1 = THIS_Value1;
	ReturnT v2 = THIS_Value2;
	ReturnT v3 = THIS_Value3;
	ReturnT v4 = THIS_Value4;

	#if defined(THIS_Weightmode_nearest)
	float d = min(min(d1, d2), min(d3, d4));
	if (d == d1) return v1;
	if (d == d2) return v2;
	if (d == d3) return v3;
	return v4;
	#elif defined(THIS_Weightmode_linearweight)
	// THIS IS INCORRECT
	float totalD = d1 + d2 + d3 + d4;
	return (v1 * ((d1 / totalD))) +
	(v2 * ((d2 / totalD))) +
	(v3 * ((d3 / totalD))) +
	(v4 * ((d4 / totalD)));
	#else
	#error invalidWeightMode
	#endif
}
