ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef RAYTK_USE_TIME
	{
		float shift = THIS_Shift;
		#ifdef THIS_HAS_INPUT_2
		shift += inputOp2(p, ctx);
		#endif
		Time time = contextTime(ctx);
		#if defined(THIS_Intervaltype_frames)
			time_setFrame(time, wrapRange(time.frame + shift, time.start, time.end));
		#elif defined(THIS_Intervaltype_seconds)
			time_setSeconds(time, wrapRange(time.seconds + shift, (time.start-1)*time.rate, (time.end-1)*time.rate));
		#elif defined(THIS_Intervaltype_absframes)
			time_setAbsFrame(time, time.absFrame + shift);
		#elif defined(THIS_Intervaltype_absseconds)
			time_setAbsSeconds(time, time.absSeconds + shift);
		#else
			#error invalidIntervalType
		#endif
		setContextTime(ctx, time);
	}
	#endif
	return inputOp1(p, ctx);
}