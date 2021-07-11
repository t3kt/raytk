ReturnT thismap(CoordT p, ContextT ctx) {
	float d;
	vec3 firstPt;
	vec3 lastPt;
	#if defined(THIS_Source_params)
	{
		firstPt = THIS_Point1;
		lastPt = THIS_Point2;
		d = fLineSegment(p, THIS_Point1, THIS_Point2);
		#if THIS_Segments > 1
		lastPt = THIS_Point3;
		d = min(d, fLineSegment(p, THIS_Point2, THIS_Point3));
		#endif
		#if THIS_Segments > 2
		lastPt = THIS_Point4;
		d = min(d, fLineSegment(p, THIS_Point3, THIS_Point4));
		#endif
		#if THIS_Segments > 3
		lastPt = THIS_Point5;
		d = min(d, fLineSegment(p, THIS_Point4, THIS_Point5));
		#endif
		#if THIS_Segments > 4
		lastPt = THIS_Point6;
		d = min(d, fLineSegment(p, THIS_Point5, THIS_Point6));
		#endif
		#if THIS_Segments > 5
		lastPt = THIS_Point7;
		d = min(d, fLineSegment(p, THIS_Point6, THIS_Point7));
		#endif
		#if THIS_Segments > 6
		lastPt = THIS_Point8;
		d = min(d, fLineSegment(p, THIS_Point7, THIS_Point8));
		#endif
	}
	#elif defined(THIS_Source_chop)
	{
		firstPt = THIS_points[0];
		lastPt = THIS_points[1];
		d = fLineSegment(p, THIS_points[0], THIS_points[1]);
		#if THIS_Segments > 1
		d = min(d, fLineSegment(p, THIS_points[1], THIS_points[2]));
		lastPt = THIS_points[2];
		#endif
		#if THIS_Segments > 2
		d = min(d, fLineSegment(p, THIS_points[2], THIS_points[3]));
		lastPt = THIS_points[3];
		#endif
		#if THIS_Segments > 3
		d = min(d, fLineSegment(p, THIS_points[3], THIS_points[4]));
		lastPt = THIS_points[4];
		#endif
		#if THIS_Segments > 4
		d = min(d, fLineSegment(p, THIS_points[4], THIS_points[5]));
		lastPt = THIS_points[5];
		#endif
		#if THIS_Segments > 5
		d = min(d, fLineSegment(p, THIS_points[5], THIS_points[6]));
		lastPt = THIS_points[6];
		#endif
		#if THIS_Segments > 6
		d = min(d, fLineSegment(p, THIS_points[6], THIS_points[7]));
		lastPt = THIS_points[7];
		#endif
	}
	#else
	#error invalidSource
	#endif
	#if defined(THIS_Closepath) && THIS_Segments > 1
		d = min(d, fLineSegment(p, lastPt, firstPt));
	#endif
	return createSdf(d - THIS_Radius);
}