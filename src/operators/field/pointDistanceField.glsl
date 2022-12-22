ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec4 q = adaptAsVec4(inputOp_coordField(p, ctx));
	#else
	vec4 q = adaptAsVec4(p);
	#endif
	#ifdef THIS_HAS_INPUT_centerField
	vec4 c = adaptAsVec4(inputOp_centerField(p, ctx));
	#else
	vec4 c = adaptAsVec4(THIS_Center);
	#endif
	float res;
	BODY();
	return res;
}