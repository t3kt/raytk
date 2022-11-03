ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT c = THIS_asCoordT(THIS_Center);
	#if defined(THIS_COORD_TYPE_vec3) && !defined(THIS_Axes_xyz)
	return length(p.THIS_Axes - c.THIS_Axes);
	#else
	return length(p - c);
	#endif
}