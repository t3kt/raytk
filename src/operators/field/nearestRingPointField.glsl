ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q;
	#if defined(THIS_HAS_INPUT_coordField)
	q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q = adaptAsVec3(p);
	#endif
	vec3 center = THIS_Center;
	float r = THIS_Radius;

	q -= center;

	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q.zyx; break;
		case THISTYPE_Axis_y: q = q.zxy; break;
		case THISTYPE_Axis_z: break;
	}

	float n = float(THIS_Points);
	float angle = TAU / n;
	float a = atan(q.y, q.x);
	float cell = floor(a / angle);

	float nearestAngle = cell * angle;

	vec3 nearestPos = vec3(
		r * cos(nearestAngle + angle / 2.),
		r * sin(nearestAngle + angle / 2.),
		0.
	);
	nearestPos += center;
	q += center;
	float d = distance(q, nearestPos);
	vec3 vec = nearestPos - q;

	#ifdef THIS_EXPOSE_pos
	THIS_pos = nearestPos;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = nearestAngle;
	#endif
	#ifdef THIS_EXPOSE_dist
	THIS_dist = d;
	#endif
	#ifdef THIS_EXPOSE_vector
	THIS_vector = vec;
	#endif
	// there's definitely a cleaner way to do this
	cell += (n / 2.);
	cell = (n-1.) - cell;
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