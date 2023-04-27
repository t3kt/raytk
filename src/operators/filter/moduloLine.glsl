ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}

	vec3 pt1 = THIS_Point1;
	vec3 pt2 = THIS_Point2;
	float divs = THIS_Divisions;
	float size = distance(pt1, pt2) / divs;
	float halfSize = size * 0.5;

	vec3 dir = normalize(pt1 - pt2);
	vec3 up = vec3(0., 1., 0.);
	if (dir == vec3(0., 1., 0.)) {
		up = vec3(0., 0., 1.);
	}
	mat3 rot = TDRotateToVector(dir, up);

	vec3 p3 = adaptAsVec3(p);
	p3 -= pt1;
	p3 = p3.zyx;
	p3 *= rot;
	p3 = p3.zyx;

	float q = p3.x;
	float c = floor((q + halfSize)/size);
	q = mod(q+halfSize, size) - halfSize;

	float start = 0.;
	float stop = divs - 1;
	if (c < start) applyModLimit(q, c, size, start);
	if (c > stop) applyModLimit(q, c, size, stop);

	p3.x = q;
	p3 = p3.zyx;
	p3 *= -rot;
	p3 = p3.zyx;
	p3 += pt1;

	p = THIS_asCoordT(p3);

	return inputOp1(p, ctx);
}