ReturnT thismap(CoordT p, ContextT ctx) {
	float d1 = length(p - THIS_Point1);
	float d2 = length(p - THIS_Point2);
	float d3 = length(p - THIS_Point3);
	float d4 = length(p - THIS_Point4);
	vec4 allD = vec4(d1, d2, d3, d4);

	ReturnT v1 = THIS_Value1;
	ReturnT v2 = THIS_Value2;
	ReturnT v3 = THIS_Value3;
	ReturnT v4 = THIS_Value4;

	ReturnT allV[4];
	allV[0] = v1;
	allV[1] = v2;
	allV[2] = v3;
	allV[3] = v4;

	#if defined(THIS_Weightmode_nearest)
//	float d = min(min(d1, d2), min(d3, d4));
//	if (d == d1) return v1;
//	if (d == d2) return v2;
//	if (d == d3) return v3;
//	return v4;
	float minD;
	int i = findMin(allD, minD);
	return allV[i];
	#elif defined(THIS_Weightmode_linearnearest)
	float minD1, minD2;
	int i2;
	int i1 = findMin(allD, minD1);
	if (i1 == 0) {
		i2 = findMin(allD.yzw, minD2);
	}
	else if (i1 == 1) {
		i2 = findMin(allD.xzw, minD2);
	}
	else if (i1 == 2) {
		i2 = findMin(allD.xyw, minD2);
	} else {
		i2 = findMin(allD.xyz, minD2);
	}
		float totalD = minD1 + minD2;
		return mix(allV[i1], allV[i2], minD1 / (minD1 + minD2));
	#elif defined(THIS_Weightmode_linearweight)
	// THIS IS INCORRECT
	float totalD = d1 + d2 + d3 + d4;
	return (v1 * (1.0 - (d1 / totalD))) +
	(v2 * (1.0 - (d2 / totalD))) +
	(v3 * (1.0 - (d3 / totalD))) +
	(v4 * (1.0 - (d4 / totalD)));
	#else
	#error invalidWeightMode
	#endif
}
