ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_point1Field
	vec3 pt1 = adaptAsVec3(inputOp_point1Field(p, ctx));
	#else
	vec3 pt1 = THIS_Point1;
	#endif
	#ifdef THIS_HAS_INPUT_point2Field
	vec3 pt2 = adaptAsVec3(inputOp_point2Field(p, ctx));
	#else
	vec3 pt2 = THIS_Point2;
	#endif
	vec3 dir = pt1 - pt2;

	vec3 up = vec3(0., 1., 0.);
	if (dir == vec3(0., 1., 0.)) {
		up = vec3(0., 0., 1.);
	}
	vec3 q = p;
	q -= pt1;
	q *= TDRotateToVector(dir, up);
	vec2 planePos = q.xy;
	float axisPos = q.z;
	float h = distance(pt1, pt2) / 2.;
	float o = -h;

	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = axisPos;
	#endif
	float ratio = saturate(map01(axisPos - o, h, -h));
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = ratio;
	#endif

	ReturnT res = inputOp_crossSection(planePos, ctx);
	vec2 w = vec2(res.x, abs(axisPos - o) - h);
	res.x = min(max(w.x, w.y), 0.) + length(max(w, 0.));

	return res;
}