ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdChain(p, THIS_Length, THIS_Radius, THIS_Thickness));
}