ReturnT thismap(CoordT p, ContextT ctx) {
	float totalWeight = THIS_Baselevel;
	vec3 totalValue = THIS_Basecolor * totalWeight;
	AGGREGATE_BODY();
	ReturnT res = vec4(totalValue, 1.0);
	COMBINE_BODY();
	return res;
}