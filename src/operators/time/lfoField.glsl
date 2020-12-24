ReturnT thismap(CoordT p, ContextT ctx) {
	Time time = THIS_TIME;
	#if defined(THIS_Intervaltype_seconds)
	float t = time.seconds;
	#elif defined(THIS_Intervaltype_frames)
	float t = time.frame;
	#elif defined(THIS_Intervaltype_absseconds)
	float t = time.absSeconds;
	#elif defined(THIS_Intervaltype_absframes)
	float t = time.absFrame;
	#else
	#error invalidIntervalType
	#endif
	t = fract((t + THIS_Phase*THIS_Period)/ THIS_Period);
	return THIS_Offset + (t * THIS_Amplitude);
}