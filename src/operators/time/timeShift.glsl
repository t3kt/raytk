ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef RAYTK_USE_TIME
	{
		float shift = THIS_Shift;
		#ifdef THIS_HAS_INPUT_shiftField
		shift += inputOp_shiftField(p, ctx);
		#endif
		Time time = contextTime(ctx);
		BODY();
		setContextTime(ctx, time);
	}
	#endif
	return inputOp1(p, ctx);
}