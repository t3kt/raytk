float THIS_totalDist;
float THIS_segmentOffsets[8];
float THIS_segmentLengths[8];

void THIS_init() {
	THIS_totalDist = 0.;
	float d;
	vec3 lastPt;
	#if defined(THIS_Source_params)
	{
		THIS_segmentOffsets[0] = 0.;
		d = distance(THIS_Point1, THIS_Point2);
		THIS_segmentLengths[0] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point2;
		#if THIS_Segments > 1
		THIS_segmentOffsets[1] = THIS_totalDist;
		d = distance(THIS_Point2, THIS_Point3);
		THIS_segmentLengths[1] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point3;
		#endif
		#if THIS_Segments > 2
		THIS_segmentOffsets[2] = THIS_totalDist;
		d = distance(THIS_Point3, THIS_Point4);
		THIS_segmentLengths[2] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point4;
		#endif
		#if THIS_Segments > 3
		THIS_segmentOffsets[3] = THIS_totalDist;
		d = distance(THIS_Point4, THIS_Point5);
		THIS_segmentLengths[3] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point5;
		#endif
		#if THIS_Segments > 4
		THIS_segmentOffsets[4] = THIS_totalDist;
		d = distance(THIS_Point5, THIS_Point6);
		THIS_segmentLengths[4] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point6;
		#endif
		#if THIS_Segments > 5
		THIS_segmentOffsets[5] = THIS_totalDist;
		d = distance(THIS_Point6, THIS_Point7);
		THIS_segmentLengths[5] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point7;
		#endif
		#if THIS_Segments > 6
		THIS_segmentOffsets[6] = THIS_totalDist;
		d = distance(THIS_Point7, THIS_Point8);
		THIS_segmentLengths[6] = d;
		THIS_totalDist += d;
		lastPt = THIS_Point8;
		#endif
		#if defined(THIS_Closepath) && THIS_Segments > 1
		THIS_segmentOffsets[7] = THIS_totalDist;
		d = distance(THIS_Point1, lastPt);
		THIS_segmentLengths[7] = d;
		THIS_totalDist += d;
		#endif
	}
	#elif defined(THIS_Source_chop)
	{
		THIS_segmentOffsets[0] = 0.;
		d = distance(THIS_points[0], THIS_points[1]);
		THIS_segmentLengths[0] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[1];
		#if THIS_Segments > 1
		THIS_segmentOffsets[1] = THIS_totalDist;
		d = distance(THIS_points[1], THIS_points[2]);
		THIS_segmentLengths[1] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[2];
		#endif
		#if THIS_Segments > 2
		THIS_segmentOffsets[2] = THIS_totalDist;
		d = distance(THIS_points[2], THIS_points[3]);
		THIS_segmentLengths[2] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[3];
		#endif
		#if THIS_Segments > 3
		THIS_segmentOffsets[3] = THIS_totalDist;
		d = distance(THIS_points[3], THIS_points[4]);
		THIS_segmentLengths[3] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[4];
		#endif
		#if THIS_Segments > 4
		THIS_segmentOffsets[4] = THIS_totalDist;
		d = distance(THIS_points[4], THIS_points[5]);
		THIS_segmentLengths[4] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[5];
		#endif
		#if THIS_Segments > 5
		THIS_segmentOffsets[5] = THIS_totalDist;
		d = distance(THIS_points[5], THIS_points[6]);
		THIS_segmentLengths[5] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[6];
		#endif
		#if THIS_Segments > 6
		THIS_segmentOffsets[6] = THIS_totalDist;
		d = distance(THIS_points[6], THIS_points[7]);
		THIS_segmentLengths[6] = d;
		THIS_totalDist += d;
		lastPt = THIS_points[7];
		#endif
		#if defined(THIS_Closepath) && THIS_Segments > 1
		THIS_segmentOffsets[7] = THIS_totalDist;
		d = distance(THIS_points[0], lastPt);
		THIS_segmentLengths[7] = d;
		THIS_totalDist += d;
		#endif
	}
	#endif
}
