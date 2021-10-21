CoordT THIS_wave(CoordT q) {
	CoordT res;
	BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_coordField)
	CoordT q = THIS_asCoordT(inputOp_coordField(p, ctx));
	#else
	CoordT q = p;
	#endif
	q = THIS_asCoordT(THIS_Phase) + (q / THIS_asCoordT(THIS_Period));
	CoordT val = THIS_asCoordT(THIS_Offset) + THIS_wave(q) * THIS_asCoordT(THIS_Amplitude);
	return adaptAsVec4(val);
}