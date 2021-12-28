ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_COORD_TYPE_float
	return abs(p - THIS_Center);
	#pragma r:else
	return length(p.THIS_AXIS - THIS_Center);
	#pragma r:endif
}