ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p;
	CoordT res;
	WAVE_PREP();
	WAVE_BODY();
	res = (res * THIS_Amplitude) + THIS_Offset;
	return THIS_asReturnT(res);
}