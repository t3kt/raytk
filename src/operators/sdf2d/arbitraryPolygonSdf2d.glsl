// https://www.shadertoy.com/view/wdBXRW

ReturnT thismap(CoordT p, ContextT ctx) {
	const int num = THIS_N;
	int ptCount;
	vec2 pts[THIS_N];
	#ifdef THIS_Source_chop
	{
		ptCount = int(THIS_choplen);
		pts = THIS_points;
	}
	#else // THIS_Source_params
	{
		ptCount = int(THIS_Pointcount);
		pts[0] = THIS_Point1;
		pts[1] = THIS_Point2;
		#if THIS_N >= 3
		pts[2]= THIS_Point3;
		#endif
		#if THIS_N >= 4
		pts[3]= THIS_Point4;
		#endif
		#if THIS_N >= 5
		pts[4]= THIS_Point5;
		#endif
		#if THIS_N >= 6
		pts[5]= THIS_Point6;
		#endif
		#if THIS_N >= 7
		pts[6]= THIS_Point7;
		#endif
		#if THIS_N >= 8
		pts[7]= THIS_Point8;
		#endif
	}
	#endif
	float d = dot2(p - pts[0]);
	float s = 1.0;
	for (int i=0, j=ptCount-1; i < num; j=i, i++) {
		if (i >= ptCount) break;
		// distance
		vec2 e = pts[j] - pts[i];
		vec2 w = p - pts[i];
		vec2 b = w - e*clamp(dot(w,e)/dot2(e), 0., 1.);
		d = min(d, dot2(b));

		// winding number from http://geomalgorithms.com/a03-_inclusion.html
		bvec3 cond = bvec3(
			p.y >= pts[i].y,
			p.y < pts[j].y,
			e.x*w.y>e.y*w.x);
		if (all(cond) || all(not(cond))) s = -s;
	}
	return createSdf(s * sqrt(d));
}