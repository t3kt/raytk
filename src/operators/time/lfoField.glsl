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
	#pragma r:if THIS_HAS_INPUT_waveFunction
	res = inputOp_waveFunction(fract(q), ctx);
	#pragma r:else
	WAVE_BODY();
	#pragma r:endif
	return THIS_Offset + (res * THIS_Amplitude);
}