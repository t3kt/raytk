ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef RAYTK_USE_TIME
	{
		float shift = THIS_Shift;
		#ifdef THIS_HAS_INPUT_2
		shift += inputOp2(p, ctx);
		#endif
		Time time = contextTime(ctx);
		#if defined(THIS_Intervaltype_frames)
			time_setFrame(time, wrapRange(time_frame(time) + shift, time_start(time), time_end(time)));
		#elif defined(THIS_Intervaltype_seconds)
			time_setSeconds(time, wrapRange(time_seconds(time) + shift, (time_start(time)-1)*time_rate(time), (time_end(time)-1)*time_rate(time)));
		#elif defined(THIS_Intervaltype_absframes)
			time_setAbsFrame(time, time_absFrame(time) + shift);
		#elif defined(THIS_Intervaltype_absseconds)
			time_setAbsSeconds(time, time_absSeconds(time) + shift);
		#else
			#error invalidIntervalType
		#endif
		setContextTime(ctx, time);
	}
	#endif
	return inputOp1(p, ctx);
}