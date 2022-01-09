ReturnT thismap(CoordT p, ContextT ctx) {
	Time time = THIS_TIME;
	#pragma r:if THIS_Intervaltype_seconds
	float x = time_seconds(time);
	#pragma r:elif THIS_Intervaltype_frames
	float x = time_frame(time);
	#pragma r:elif THIS_Intervaltype_absseconds
	float x = time_absSeconds(time);
	#pragma r:elif THIS_Intervaltype_absframes
	float x = time_absFrame(time);
	#pragma r:else
	#error invalidIntervalType
	#pragma r:endif
	x = fract((x + THIS_Phase*THIS_Period)/ THIS_Period);
	if (THIS_Reverse > 0.) {
		x = 1.0 - x;
	}
	ReturnT res;
	#pragma r:if THIS_HAS_INPUT_waveFunction
	res = inputOp_waveFunction(x, ctx);
	#pragma r:else
	res = THIS_WAVE_EXPR;
	#pragma r:endif
	return THIS_Offset + (res * THIS_Amplitude);
}