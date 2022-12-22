void THIS_apply(inout CoordT p, inout ContextT ctx) {
	vec3 center = THIS_Center;
	float d;
	#ifdef THIS_COORD_TYPE_vec2
	p += center.xy;
	d = length(p);
	#else
	switch (int(THIS_Distancemode)) {
		case THISTYPE_Distancemode_xaxis:
			p.yz += center.yz;
			d = length(p.yz);
			break;
		case THISTYPE_Distancemode_yaxis:
			p.zx += center.zx;
			d = length(p.zx);
			break;
		case THISTYPE_Distancemode_zaxis:
			p.xy += center.xy;
			d = length(p.xy);
			break;
		case THISTYPE_Distancemode_spherical:
			p += center;
			d = length(p);
			break;
	}
	#endif

	float cell;
	if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
		cell = pModMirror1(d, THIS_Length);
	} else {
		cell = pMod1(d, THIS_Length*.5);
	}

	#ifdef THIS_CONTEXT_TYPE_Context
	if (IS_TRUE(THIS_Iterateonrings)) {
		setIterationIndex(ctx, cell);
	}
	#endif

	#ifdef THIS_EXPOSE_ring
	THIS_ring = cell;
	#endif

	#ifdef THIS_COORD_TYPE_vec2
	float a = atan(p.y, p.x);
	p = d * vec2(cos(a), sin(a)) - center.xy;
	#else
	vec2 q;
	float a;
	switch (int(THIS_Distancemode)) {
		case THISTYPE_Distancemode_spherical:
			float alpha = atan(p.y, p.x);
			float polar = atan(p.x, p.z);
			p = d * vec3(
				sin(polar) * cos(alpha),
				sin(polar) * sin(alpha),
				cos(polar)) - center;
			break;
		case THISTYPE_Distancemode_xaxis:
			q = p.yz;
			a = atan(q.y, q.x);
			p.yz = d * vec2(cos(a), sin(a)) - center.yz;
			break;
		case THISTYPE_Distancemode_yaxis:
			q = p.zx;
			a = atan(q.y, q.x);
			p.zx = d * vec2(cos(a), sin(a)) - center.zx;
			break;
		case THISTYPE_Distancemode_zaxis:
			q = p.xy;
			a = atan(q.y, q.x);
			p.xy = d * vec2(cos(a), sin(a)) - center.xy;
			break;
	}
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}