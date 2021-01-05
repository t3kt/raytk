float thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_float
	return abs(p - THIS_Center);
	#else
	return length(p.THIS_AXIS - THIS_Center);
	#endif
}