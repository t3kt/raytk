ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	vec4 pts = inputOp1(p, ctx);
	vec2 pt1 = pts.xy;
	vec2 pt2 = pts.zw;
	#else
	vec2 pt1 = THIS_Pointa;
	vec2 pt2 = THIS_Pointb;
	#endif
	return createSdf(sdSegment(p, pt1, pt2));
}