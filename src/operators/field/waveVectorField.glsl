CoordT THIS_wave(CoordT q) {
	CoordT res;
	BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
	CoordT q = THIS_asCoordT(inputOp_coordField(p, ctx));
	#pragma r:else
	CoordT q = p;
	#pragma r:endif
	q = THIS_asCoordT(THIS_Phase) + (q / THIS_asCoordT(THIS_Period));
	CoordT val = THIS_asCoordT(THIS_Offset) + THIS_wave(q) * THIS_asCoordT(THIS_Amplitude);
	return adaptAsVec4(val);
}