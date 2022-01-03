ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p;
	CoordT res;
	WAVE();
	res = (res * THIS_Amplitude) + THIS_Offset;
	return THIS_asReturnT(res);
}