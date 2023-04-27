ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		#ifdef THIS_EXPOSE_cellcoord
		THIS_cellcoord = 0;
		#endif
		#ifdef THIS_EXPOSE_normcoord
		THIS_normcoord = 0.;
		#endif
		return inputOp1(p, ctx);
	}

	vec3 pt1 = THIS_Point1;
	vec3 pt2 = THIS_Point2;
	float divs = THIS_Divisions;
	float size = distance(pt1, pt2) / (divs-1.);
	float halfSize = size * 0.5;

	vec3 dir = normalize(pt1 - pt2);
	vec3 up = vec3(0., 1., 0.);
	if (dir == vec3(0., 1., 0.)) {
		up = vec3(0., 0., 1.);
	}
	mat3 rot = TDRotateToVector(dir, up);

	vec3 p3 = adaptAsVec3(p);
	p3 -= pt1;
	p3 *= rot;

	float q = p3.z;
	float c = floor((q + halfSize)/size);
	q = mod(q+halfSize, size) - halfSize;

	float start = -divs + 1.;
	float stop = 0.;
	if (c < start) applyModLimit(q, c, size, start);
	if (c > stop) applyModLimit(q, c, size, stop);

	p3.z = q;
	p = THIS_asCoordT(p3.zyx);

	c *= -1.;
	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = int(c);
	#endif
	#ifdef THIS_EXPOSE_normcoord
	THIS_normcoord = c / (divs - 1.);
	#endif
	return inputOp1(p, ctx);
}