ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	float level = ctx.shadedLevel;
	if (THIS_Invert > 0.) {
		level = 1.0 - level;
	}

	#pragma r:if THIS_Usecolor
	res = vec4(THIS_Color * level, 1.);
	#pragma r:else
	res = level;
	#pragma r:endif
	return res;
}