ReturnT thismap(CoordT p, ContextT ctx) {
	p = (p / THIS_Period) + THIS_Phase;
	CoordT res;
	BODY();
	res = (res * THIS_Amplitude) + THIS_Offset;
	return THIS_asReturnT(res);
}