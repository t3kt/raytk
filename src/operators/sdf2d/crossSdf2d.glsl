ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdCross(p, vec2(THIS_Outersize, THIS_Innersize), THIS_Roundness));
}