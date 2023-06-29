// https://www.shadertoy.com/view/4tySDW
// a lovely function that goes up and down periodically between 0 and 1, pausing at the extremes
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_lowWidthField
	float a = inputOp_lowWidthField(p, ctx);
	#else
	float a = THIS_Lowwidth;
	#endif
	#ifdef THIS_HAS_INPUT_highWidthField
	float b = inputOp_highWidthField(p, ctx);
	#else
	float b = THIS_Highwidth;
	#endif
	float x = abs(fract(p) - .5) * 1. - .5 + a;
	return smoothstep(0., a - b, x);
}