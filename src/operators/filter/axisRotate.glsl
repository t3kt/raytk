void THIS_transform(inout vec4 q, in CoordT p, inout ContextT ctx) {
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_rotateField
	r += radians(inputOp_rotateField(p, ctx));
	#endif
	switch (int(THIS_Axis)) {
		case 0: pR(q.yz, r); break;
		case 1: pR(q.zx, r); break;
		case 2: pR(q.xy, r); break;
	}
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	} else {
		#ifdef THIS_HAS_INPUT_1
		res = inputOp1(p, ctx);
		#endif
	}
	#ifdef THIS_HAS_INPUT_1
	return res;
	#else
	return q;
	#endif
}