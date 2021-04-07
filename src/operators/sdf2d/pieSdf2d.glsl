ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p, THIS_Rotate);
	return createSdf(sdPie(p, THIS_C, THIS_Radius));
}