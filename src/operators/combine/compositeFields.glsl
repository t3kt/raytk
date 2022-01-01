ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = fillToVec4(inputOp1(p, ctx));
	ReturnT res2 = fillToVec4(inputOp2(p, ctx));
	if (THIS_Swapinputs > 0.) {
		ReturnT tmp = res1;
		res1 = res2;
		res2 = tmp;
	}
	vec3 col1 = res1.rgb;
	vec3 col2 = res2.rgb;
	float amt = THIS_Blend;
	vec3 col;
	BODY();
	return vec4(col, mix(res1.a, res2.a, amt));
}