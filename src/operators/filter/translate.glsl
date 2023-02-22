void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	q.xyz -= THIS_Translate;
	#ifdef THIS_HAS_INPUT_translateField
	q.xyz -= adaptAsVec3(inputOp_translateField(p, ctx));
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	}
	#ifdef THIS_HAS_INPUT_1
	return res;
	#else
	return q;
	#endif
}