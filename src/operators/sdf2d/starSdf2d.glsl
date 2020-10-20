ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdStar(p, THIS_Radius, THIS_Points, THIS_M));
}