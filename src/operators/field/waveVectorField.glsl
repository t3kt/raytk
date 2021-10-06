CoordT THIS_wave(CoordT q) {
	CoordT res;
	BODY();
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = THIS_asCoordT(THIS_Phase) + (p / THIS_asCoordT(THIS_Period));
	CoordT val = THIS_asCoordT(THIS_Offset) + THIS_wave(q) * THIS_asCoordT(THIS_Amplitude);
	return adaptAsVec4(val);
}