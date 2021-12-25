ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_inputOp1
	vec2 a = adaptAsVec2(inputOp1(p, ctx));
	#else
	vec2 a = adaptAsVec2(p);
	#endif
	#ifdef THIS_HAS_INPUT_inputOp2
	vec2 b = adaptAsVec2(inputOp2(p, ctx));
	#else
	vec2 b = vec2(0.);
	#endif
	THIS_ValueT val;
	BODY();
	ReturnT res = adaptAsVec4(val);
	return res;
}