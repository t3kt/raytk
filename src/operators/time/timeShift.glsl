ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if RAYTK_USE_TIME
	{
		float shift = THIS_Shift;
		#pragma r:if THIS_HAS_INPUT_shiftField
		shift += inputOp_shiftField(p, ctx);
		#pragma r:endif
		Time time = contextTime(ctx);
		BODY();
		setContextTime(ctx, time);
	}
	#pragma r:endif
	return inputOp1(p, ctx);
}