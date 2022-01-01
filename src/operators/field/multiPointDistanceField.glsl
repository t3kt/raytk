ReturnT thismap(CoordT p, ContextT ctx) {
	return vec4(
		length(p - THIS_Point1),
		length(p - THIS_Point2),
		length(p - THIS_Point3),
		length(p - THIS_Point4));
}