void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return;
	q = adaptAsVec4(inputOp_transform(THIS_asCoordT(q), ctx));
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	vec4 q;
	ReturnT res;
	APPLY_TO_TARGET();
	return res;
}