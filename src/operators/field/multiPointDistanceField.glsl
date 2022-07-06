ReturnT thismap(CoordT p, ContextT ctx) {
	return vec4(
		length(p - THIS_asCoordT(THIS_Point1)),
		length(p - THIS_asCoordT(THIS_Point2)),
		length(p - THIS_asCoordT(THIS_Point3)),
		length(p - THIS_asCoordT(THIS_Point4)));
}