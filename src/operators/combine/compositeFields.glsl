ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Swapinputs
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	#else
	ReturnT res1 = inputOp2(p, ctx);
	ReturnT res2 = inputOp1(p, ctx);
	#endif
	vec3 col1 = res1.rgb;
	vec3 col2 = res2.rgb;
	float amt = THIS_Blend;
	vec3 col = THIS_EXPR;
	return vec4(col, mix(res1.a, res2.a, amt));
}