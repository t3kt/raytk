ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_CAPPED
	return createSdf(sdCappedTorus(
		p - THIS_Translate, vec2(THIS_Startangle, THIS_Endangle), THIS_Radius, THIS_Thickness));
	#else
	return createSdf(fTorus(p - THIS_Translate, THIS_Thickness, THIS_Radius));
	#endif
}