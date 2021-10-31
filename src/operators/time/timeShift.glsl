ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if RAYTK_USE_TIME
	{
		float shift = THIS_Shift;
		#pragma r:if THIS_HAS_INPUT_shiftField
		shift += inputOp_shiftField(p, ctx);
		#pragma r:endif
		Time time = contextTime(ctx);
		#pragma r:if THIS_Intervaltype_frames
			time_setFrame(time, wrapRange(time_frame(time) + shift, time_start(time), time_end(time)));
		#pragma r:elif THIS_Intervaltype_seconds
			time_setSeconds(time, wrapRange(time_seconds(time) + shift, (time_start(time)-1)*time_rate(time), (time_end(time)-1)*time_rate(time)));
		#pragma r:elif THIS_Intervaltype_absframes
			time_setAbsFrame(time, time_absFrame(time) + shift);
		#pragma r:elif THIS_Intervaltype_absseconds
			time_setAbsSeconds(time, time_absSeconds(time) + shift);
		#pragma r:else
			#error invalidIntervalType
		#pragma r:endif
		setContextTime(ctx, time);
	}
	#pragma r:endif
	return inputOp1(p, ctx);
}