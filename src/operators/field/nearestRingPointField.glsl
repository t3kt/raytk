ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q;
	#if defined(THIS_HAS_INPUT_coordField)
	q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q = adaptAsVec3(p);
	#endif
	vec3 center = THIS_Center;
	float r = THIS_Radius;
	float rot = THIS_Rotate;

	q -= center;

	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q.zyx; break;
		case THISTYPE_Axis_y: q = q.zxy; break;
		case THISTYPE_Axis_z: break;
	}

	pR(q.xy, rot);

	float n = float(THIS_Points);
	float angle = TAU / n;
	float a = atan(q.y, q.x) + angle / 2.;
	float cell = floor(a / angle);
	// there's definitely a cleaner way to do this
	if (cell < 0.) {
		cell = mapRange(cell, -n/2., 0., n/2., n);
	}

	float nearestAngle = cell * angle;

	vec3 nearestPos = vec3(
		r * cos(nearestAngle),
		r * sin(nearestAngle),
		0.
	);
	pR(q.xy, -rot);
	pR(nearestPos.xy, -rot);
	nearestPos += center;
	q += center;
	float d = distance(q, nearestPos);
	vec3 vec = nearestPos - q;

	#ifdef THIS_EXPOSE_pos
	THIS_pos = nearestPos;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = cell * degrees(angle);
	#endif
	#ifdef THIS_EXPOSE_dist
	THIS_dist = d;
	#endif
	#ifdef THIS_EXPOSE_vector
	THIS_vector = vec;
	#endif
	#ifdef THIS_EXPOSE_step
	THIS_step = int(cell);
	#endif
	#ifdef THIS_EXPOSE_normstep
	THIS_normstep = cell / (n - 1.);
	#endif

	ReturnT res;
	FORMAT_BODY();
	return res;
}