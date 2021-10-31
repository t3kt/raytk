ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#pragma r:if THIS_Mode_centered
	res = createSdf(sdTrapezoid(p, THIS_Width2, THIS_Width1, THIS_Height));
	#pragma r:elif THIS_Mode_endpoints
	res = createSdf(sdTrapezoid(p, THIS_Point1, THIS_Point2, THIS_Width1, THIS_Width2));
	#pragma r:else
	#error invalidMode
	#pragma r:endif
	return res;
}