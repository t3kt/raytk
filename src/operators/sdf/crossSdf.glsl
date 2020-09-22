Sdf thismap(CoordT p, ContextT ctx) {
	return createSdf(sdCrossSmooth(p - THIS_Translate, THIS_Size, THIS_Smoothradius));
}