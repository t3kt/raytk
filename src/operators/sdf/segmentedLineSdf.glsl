void THIS_expose(vec3 p, int segment, vec3 ptA, vec3 ptB, float segmentLength, float segmentOffset) {
	#ifdef THIS_EXPOSE_stepindex
	THIS_stepindex = segment;
	#endif
	#ifdef THIS_EXPOSE_normstepindex
	THIS_normstepindex = float(segment) / float(THIS_Segments);
	#endif
	float localDist = length(dot(p - ptA, ptB - ptA));
	#ifdef THIS_EXPOSE_stepinterp
	THIS_stepinterp = float(segment) + (localDist / segmentLength);
	#endif
	#ifdef THIS_EXPOSE_offset
	THIS_offset = segmentOffset + localDist;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = (segmentOffset + localDist) / THIS_totalDist;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float d;
	vec3 firstPt;
	vec3 lastPt;
	float rBase = THIS_Radius;
	float r;
	#if defined(THIS_Source_params)
	{
		firstPt = THIS_Point1;
		lastPt = THIS_Point2;
		THIS_expose(p, 0, THIS_Point1, THIS_Point2, THIS_segmentLengths[0], THIS_segmentOffsets[0]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = fLineSegment(p, THIS_Point1, THIS_Point2) - r;
		#if THIS_Segments > 1
		lastPt = THIS_Point3;
		THIS_expose(p, 1, THIS_Point2, THIS_Point3, THIS_segmentLengths[1], THIS_segmentOffsets[1]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point2, THIS_Point3) - r);
		#endif
		#if THIS_Segments > 2
		lastPt = THIS_Point4;
		THIS_expose(p, 2, THIS_Point3, THIS_Point4, THIS_segmentLengths[2], THIS_segmentOffsets[2]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point3, THIS_Point4) - r);
		#endif
		#if THIS_Segments > 3
		lastPt = THIS_Point5;
		THIS_expose(p, 3, THIS_Point4, THIS_Point5, THIS_segmentLengths[3], THIS_segmentOffsets[3]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point4, THIS_Point5) - r);
		#endif
		#if THIS_Segments > 4
		lastPt = THIS_Point6;
		THIS_expose(p, 4, THIS_Point5, THIS_Point6, THIS_segmentLengths[4], THIS_segmentOffsets[4]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point5, THIS_Point6) - r);
		#endif
		#if THIS_Segments > 5
		lastPt = THIS_Point7;
		THIS_expose(p, 5, THIS_Point6, THIS_Point7, THIS_segmentLengths[5], THIS_segmentOffsets[5]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point6, THIS_Point7) - r);
		#endif
		#if THIS_Segments > 6
		lastPt = THIS_Point8;
		THIS_expose(p, 6, THIS_Point7, THIS_Point8, THIS_segmentLengths[7], THIS_segmentOffsets[7]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_Point7, THIS_Point8) - r);
		#endif
	}
	#elif defined(THIS_Source_chop)
	{
		firstPt = THIS_points[0];
		lastPt = THIS_points[1];
		THIS_expose(p, 0, THIS_points[0], THIS_points[1], THIS_segmentLengths[0], THIS_segmentOffsets[0]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = fLineSegment(p, THIS_points[0], THIS_points[1]) - r;
		#if THIS_Segments > 1
		THIS_expose(p, 1, THIS_points[1], THIS_points[2], THIS_segmentLengths[1], THIS_segmentOffsets[1]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[1], THIS_points[2]) - r);
		lastPt = THIS_points[2];
		#endif
		#if THIS_Segments > 2
		THIS_expose(p, 2, THIS_points[2], THIS_points[3], THIS_segmentLengths[2], THIS_segmentOffsets[2]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[2], THIS_points[3]) - r);
		lastPt = THIS_points[3];
		#endif
		#if THIS_Segments > 3
		THIS_expose(p, 3, THIS_points[3], THIS_points[4], THIS_segmentLengths[3], THIS_segmentOffsets[3]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[3], THIS_points[4]) - r);
		lastPt = THIS_points[4];
		#endif
		#if THIS_Segments > 4
		THIS_expose(p, 4, THIS_points[4], THIS_points[5], THIS_segmentLengths[4], THIS_segmentOffsets[4]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[4], THIS_points[5]) - r);
		lastPt = THIS_points[5];
		#endif
		#if THIS_Segments > 5
		THIS_expose(p, 5, THIS_points[5], THIS_points[6], THIS_segmentLengths[5], THIS_segmentOffsets[5]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[5], THIS_points[6]) - r);
		lastPt = THIS_points[6];
		#endif
		#if THIS_Segments > 6
		THIS_expose(p, 6, THIS_points[6], THIS_points[7], THIS_segmentLengths[6], THIS_segmentOffsets[6]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, THIS_points[6], THIS_points[7]) - r);
		lastPt = THIS_points[7];
		#endif
	}
	#else
	#error invalidSource
	#endif
	#if defined(THIS_Closepath) && THIS_Segments > 1
		THIS_expose(p, THIS_Segments, lastPt, firstPt, THIS_segmentLengths[7], THIS_segmentOffsets[7]);
		r = rBase;
		#ifdef THIS_HAS_INPUT_radiusField
		r *= inputOp_radiusField(p, ctx);
		#endif
		d = min(d, fLineSegment(p, lastPt, firstPt) - r);
	#endif
	return createSdf(d);
}