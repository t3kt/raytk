ReturnT thismap(CoordT p, ContextT ctx) {
	float d = fLineSegment(p, THIS_Point1, THIS_Point2);
	#if THIS_Segments > 1
	d = min(d, fLineSegment(p, THIS_Point2, THIS_Point3));
	#endif
	#if THIS_Segments > 2
	d = min(d, fLineSegment(p, THIS_Point3, THIS_Point4));
	#endif
	#if THIS_Segments > 3
	d = min(d, fLineSegment(p, THIS_Point4, THIS_Point5));
	#endif
	#if THIS_Segments > 4
	d = min(d, fLineSegment(p, THIS_Point5, THIS_Point6));
	#endif
	#if THIS_Segments > 5
	d = min(d, fLineSegment(p, THIS_Point6, THIS_Point7));
	#endif
	return createSdf(d - THIS_Radius);
}