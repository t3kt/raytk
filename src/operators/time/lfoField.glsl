ReturnT thismap(CoordT p, ContextT ctx) {
	Time time;
	GET_TIME();
	float q;
	GET_INTERVAL();
	WAVE_PREP();
	if (THIS_Reverse > 0.) {
		q = 1.0 - q;
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_waveFunction
	res = inputOp_waveFunction(fract(q), ctx);
	#else
	WAVE_BODY();
	#endif
	return THIS_Offset + (res * THIS_Amplitude);
}