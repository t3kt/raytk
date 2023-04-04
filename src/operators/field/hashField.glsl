ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q;
	#ifdef THIS_HAS_INPUT_coordField
	q = adaptAsVec4(inputOp_coordField(p, ctx));
	#else
	q = adaptAsVec4(p);
	#endif
	// TODO: axis selection
	THIS_OutputT outVal;
	BODY();
	ReturnT res = THIS_asReturnT(outVal);
	return res;
}