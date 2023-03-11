// Distance to Polyspline by oneshade
// https://www.shadertoy.com/view/7lf3Rn

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Source_params
	vec2[THIS_Segments + 1] pts;
	pts[0] = THIS_Point1;
	pts[1] = THIS_Point2;
	#if THIS_Segments >= 2
	pts[2] = THIS_Point3;
	#endif
	#if THIS_Segments >= 3
	pts[3] = THIS_Point4;
	#endif
	#if THIS_Segments >= 4
	pts[4] = THIS_Point5;
	#endif
	#if THIS_Segments >= 5
	pts[5] = THIS_Point6;
	#endif
	#if THIS_Segments >= 6
	pts[6] = THIS_Point7;
	#endif
	#else
	vec2[THIS_Segments + 1] pts = THIS_points;
	#endif
	float r = THIS_Radius;

	const int N = THIS_Segments+1;

	// Complete the first segment of the polyspline
	vec2 v1 = pts[0], v2 = vec2(0.0), v3 = 0.5 * (pts[1] + v1);
	vec2 pa = p - v1, ba = v3 - v1;
	float d = dot2(pa - ba * clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0));

	// Combine distances to quadratic beziers spanning each corner (vertex)
	for (int n=1; n < N - 1; n++) {
		v1 = 0.5 * (pts[n - 1] + pts[n]), v2 = pts[n], v3 = 0.5 * (pts[n] + pts[n + 1]);

		vec2 c1 = p - v1;
		vec2 c2 = 2.0 * v2 - v3 - v1;
		vec2 c3 = v1 - v2;

		// Solve a cubic to minimize the distance for the parameter
		float t3 = dot(c2, c2);
		float t2 = dot(c3, c2) * 3.0 / t3;
		float t1 = (dot(c1, c2) + 2.0 * dot(c3, c3)) / t3;
		float t0 = dot(c1, c3) / t3;

		float t22 = t2 * t2;
		vec2 pq = vec2(t1 - t22 / 3.0, t22 * t2 / 13.5 - t2 * t1 / 3.0 + t0);
		float ppp = pq.x * pq.x * pq.x, qq = pq.y * pq.y;

		float p2 = abs(pq.x);
		float r1 = 1.5 / pq.x * pq.y;

		if (qq * 0.25 + ppp / 27.0 > 0.0) {
			float r2 = r1 * sqrt(3.0 / p2), root;
			if (pq.x < 0.0) root = sign(pq.y) * cosh(acosh(r2 * -sign(pq.y)) / 3.0);
			else root = sinh(asinh(r2) / 3.0);
			root = clamp(-2.0 * sqrt(p2 / 3.0) * root - t2 / 3.0, 0.0, 1.0);
			d = min(d, dot2(p - mix(mix(v1, v2, root), mix(v2, v3, root), root)));
		}

		else {
			float ac = acos(r1 * sqrt(-3.0 / pq.x)) / 3.0;
			vec2 roots = clamp(2.0 * sqrt(-pq.x / 3.0) * cos(vec2(ac, ac - 4.18879020479)) - t2 / 3.0, 0.0, 1.0);
			d = min(d, dot2(p - mix(mix(v1, v2, roots.x), mix(v2, v3, roots.x), roots.x)));
			d = min(d, dot2(p - mix(mix(v1, v2, roots.y), mix(v2, v3, roots.y), roots.y)));
		}
	}

	// Complete the last segment of the polyspline
	v1 = pts[N - 1], v2 = vec2(0.0), v3 = 0.5 * (pts[N - 2] + v1);
	pa = p - v1, ba = v3 - v1;
	d = min(d, dot2(pa - ba * clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0)));

	return createSdf(sqrt(d) - r);
}