ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if defined(THIS_Mode_centered)
	res = createSdf(sdTrapezoid(p, THIS_Width2, THIS_Width1, THIS_Height));
	#elif defined(THIS_Mode_endpoints)
	res = createSdf(sdTrapezoid(p, THIS_Point1, THIS_Point2, THIS_Width1, THIS_Width2));
	#else
	#error invalidMode
	#endif
	return res;
}