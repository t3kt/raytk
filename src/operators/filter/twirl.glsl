ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return inputOp1(p, ctx);

	vec3 p3 = adaptAsVec3(p);
	vec2 q;
	float ap;
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: q = p3.yz; ap = p3.x; break;
		case THISTYPE_Axis_y: q = p3.zx; ap = p3.y; break;
		case THISTYPE_Axis_z: q = p3.xy; ap = p3.z; break;
	}

	vec2 center = THIS_Center;
	float size = THIS_Size;
	float amount = THIS_Amount;

	q += center;

	float r = length(q);
	float phi = atan(q.y, q.x);

	phi = phi + (1.0 - smoothstep(-size, size, r)) * amount;

	q.x = r * cos(phi);
	q.y = r * sin(phi);

	q -= center;

	switch (THIS_Axis) {
		case THISTYPE_Axis_x: p3.yz = q; break;
		case THISTYPE_Axis_y: p3.zx = q; break;
		case THISTYPE_Axis_z: p3.xy = q; break;
	}
	p = THIS_asCoordT(p3);
	return inputOp1(p, ctx);
}