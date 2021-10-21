ReturnT thismap(CoordT p, ContextT ctx) {
	Time time = THIS_TIME;
	#if defined(THIS_Intervaltype_seconds)
	float x = time_seconds(time);
	#elif defined(THIS_Intervaltype_frames)
	float x = time_frame(time);
	#elif defined(THIS_Intervaltype_absseconds)
	float x = time_absSeconds(time);
	#elif defined(THIS_Intervaltype_absframes)
	float x = time_absFrame(time);
	#else
	#error invalidIntervalType
	#endif
	x = fract((x + THIS_Phase*THIS_Period)/ THIS_Period);
	if (THIS_Reverse > 0.) {
		x = 1.0 - x;
	}
	#ifdef THIS_HAS_INPUT_waveFunction
	x = inputOp_waveFunction(x, ctx);
	#else
	x = THIS_WAVE_EXPR;
	#endif
	return THIS_Offset + (x * THIS_Amplitude);
}