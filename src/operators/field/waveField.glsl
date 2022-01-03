ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
		float q = inputOp_coordField(p, ctx);
	#pragma r:elif THIS_COORD_TYPE_float
		float q = p;
	#pragma r:elif THIS_Axis_dist
		float q = length(p);
	#pragma r:else
		float q = p.THIS_Axis;
	#pragma r:endif
	ReturnT res;
	WAVE();
	return (res * THIS_Amplitude) + THIS_Offset;
}