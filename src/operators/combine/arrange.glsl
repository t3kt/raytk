ReturnT THIS_combine(ReturnT res1, ReturnT res2) {
	#pragma r:if THIS_HAS_RADIUS
	float r = THIS_Radius;
	#pragma r:else
	const float r = 0;
	#pragma r:endif
	#pragma r:if THIS_HAS_NUMBER
	float n = THIS_Number;
	#pragma r:endif
	#pragma r:if THIS_HAS_OFFSET
	float o = THIS_Offset;
	#pragma r:endif
	float h = smoothBlendRatio(res1.x, res2.x, r);
	COMBINE();
	return res1;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	BODY();
	return res;
}