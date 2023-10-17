// Rectangle Repetitions by iq
// https://www.shadertoy.com/view/ctjyWy

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	vec2 q;
	#ifdef THIS_COORD_TYPE_vec2
	q = p;
	#else
	switch (THIS_Plane) {
		case THISTYPE_Plane_xy: q = p.xy; break;
		case THISTYPE_Plane_yz: q = p.yz; break;
		case THISTYPE_Plane_zx: q = p.zx; break;
	}
	#endif

	float spacing = THIS_Spacing;
	ivec2 size = ivec2(THIS_Gridsize);

	q = abs(q/spacing) - (vec2(size)*0.5-0.5);
	q = (q.x<q.y) ? q.yx : q.xy;
	q.y -= min(0.0, round(q.y));
	q *= spacing;

	#ifdef THIS_COORD_TYPE_vec2
	p = q;
	#else
	switch (THIS_Plane) {
		case THISTYPE_Plane_xy: p.xy = q; break;
		case THISTYPE_Plane_yz: p.yz = q; break;
		case THISTYPE_Plane_zx: p.zx = q; break;
	}
	#endif

	return inputOp1(p, ctx);
}