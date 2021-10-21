ReturnT THIS_combine(ReturnT res1, ReturnT res2) {
	#ifdef THIS_HAS_RADIUS
	float r = THIS_Radius;
	#else
	float r = 0;
	#endif
	#ifdef THIS_HAS_NUMBER
	float n = THIS_Number;
	#endif
	#ifdef THIS_HAS_OFFSET
	float o = THIS_Offset;
	#endif
	float h = smoothBlendRatio(res1.x, res2.x, r);
	COMBINE();
	return res1;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	BODY();
	return res;
}