ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_periodField
	float period = THIS_Period * inputOp_periodField(p, ctx);
	#pragma r:else
	float period = THIS_Period;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_coordField
		float q = inputOp_coordField(p, ctx);
	#pragma r:elif THIS_COORD_TYPE_float
		float q = p;
	#pragma r:elif THIS_Axis_dist
		float q = length(p);
	#pragma r:else
		float q = p.THIS_Axis;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_phaseField
	float phase = THIS_Phase + inputOp_phaseField(p, ctx);
	#pragma r:else
	float phase = THIS_Phase;
	#pragma r:endif
	q = (q / period) + phase;
	ReturnT res;
	BODY();
	return (res * THIS_Amplitude) + THIS_Offset;
}