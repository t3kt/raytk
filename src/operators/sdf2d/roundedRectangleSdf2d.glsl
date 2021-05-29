ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdRoundedBox(p, THIS_Scale, THIS_Roundness));
}