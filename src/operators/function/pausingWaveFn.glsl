// https://www.shadertoy.com/view/4tySDW
// a lovely function that goes up and down periodically between 0 and 1, pausing at the extremes
ReturnT thismap(CoordT p, ContextT ctx) {
	float a = THIS_Lowwidth;
	float b = THIS_Highwidth;
	float x = abs(fract(p) - .5) * 1. - .5 + a;
	return smoothstep(0., a - b, x);
}