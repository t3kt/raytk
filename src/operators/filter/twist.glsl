ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		pR(p.THIS_PLANE, p.THIS_AXIS * THIS_Amount + THIS_Shift);
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}