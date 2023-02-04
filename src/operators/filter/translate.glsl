ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		CoordT t = THIS_asCoordT(THIS_Translate);
		#ifdef THIS_HAS_INPUT_translateField
		t += THIS_asCoordT(inputOp_translateField(p, ctx));
		#endif
		p -= t;
	}
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return adaptAsVec4(p);
	#endif
}