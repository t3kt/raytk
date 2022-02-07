ReturnT thismap(CoordT p, ContextT ctx) {
	Time time = THIS_TIME;
	#pragma r:if THIS_Intervaltype_seconds
	float q = time_seconds(time);
	#pragma r:elif THIS_Intervaltype_frames
	float q = time_frame(time);
	#pragma r:elif THIS_Intervaltype_absseconds
	float q = time_absSeconds(time);
	#pragma r:elif THIS_Intervaltype_absframes
	float q = time_absFrame(time);
	#pragma r:else
	#error invalidIntervalType
	#pragma r:endif
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