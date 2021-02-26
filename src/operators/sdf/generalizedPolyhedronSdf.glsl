ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Useexponent
		return createSdf(fGDF(p - THIS_Translate, THIS_Radius, THIS_Exponent, int(THIS_BEGIN), int(THIS_END)));
	#else
		return createSdf(fGDF(p - THIS_Translate, THIS_Radius, int(THIS_BEGIN), int(THIS_END)));
	#endif
}