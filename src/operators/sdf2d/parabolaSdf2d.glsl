ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdParabola(p, 1./THIS_Width));
}