void THIS_apply(inout CoordT p, inout ContextT ctx) {
	CoordT center = THIS_asCoordT(THIS_Center);
	#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_Distancemode_spherical)
	p += center;
	float d = length(p);
	#else
	p.THIS_PLANE += center.THIS_PLANE;
	float d = length(p.THIS_PLANE);
	#endif

	float cell;
	if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
		cell = pModMirror1(d, THIS_Length);
	} else {
		cell = pMod1(d, THIS_Length*.5);
	}

	#ifdef THIS_CONTEXT_TYPE_Context
	if (THIS_Iterateonrings) {
		setIterationIndex(ctx, cell);
	}
	#endif

	#ifdef THIS_EXPOSE_ring
	THIS_ring = cell;
	#endif

	#if defined(THIS_COORD_TYPE_vec2)
	float a = atan(p.y, p.x);
	p = d * vec2(cos(a), sin(a)) - center;
	#else
	if (THIS_Distancemode == THISTYPE_Distancemode_spherical) {
		float alpha = atan(p.y, p.x);
		float polar = atan(p.x, p.z);
		p = d * vec3(
		sin(polar) * cos(alpha),
		sin(polar) * sin(alpha),
		cos(polar)) - center;
	} else {
		vec2 q = p.THIS_PLANE;
		float a = atan(q.y, q.x);
		p.THIS_PLANE = d * vec2(cos(a), sin(a)) - center.THIS_PLANE;
	}
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}