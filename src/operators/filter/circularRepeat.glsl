// Circle Repetition SDF by iq
// https://www.shadertoy.com/view/fdVBDw

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	float cs = THIS_Cellsize;
	float ra = THIS_Radius/cs;

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

	// make grid
	vec2 id0 = round(q/cs);

	// snap to circle
	if (dot2(id0) > ra*ra) id0 = round(normalize(id0) * ra);

	Sdf res = createNonHitSdf();

	// scan neighbors
	// TODO: maybe increase search window for large values for ra?
	int window = 2;
	for (int j = -window; j <= window; j++)
	for (int i = -window; i <= window; i++) {
		vec2 id = id0 + vec2(i, j);
		if (dot2(id) <= ra*ra) {
			#ifdef THIS_EXPOSE_cellcoord
			THIS_cellcoord = ivec2(id);
			#endif
			#ifdef THIS_EXPOSE_cellchecker
			THIS_cellchecker = mod(id.x+id.y, 2.) > .5;
			#endif

			vec2 q1 = q - cs*id;
			#ifdef THIS_COORD_TYPE_vec2
			vec2 localP = q1;
			#else
			CoordT localP = p;
			switch (THIS_Plane) {
				case THISTYPE_Plane_xy: localP.xy = q1; break;
				case THISTYPE_Plane_yz: localP.yz = q1; break;
				case THISTYPE_Plane_zx: localP.zx = q1; break;
			}
			#endif
			res = cmb_simpleUnion(res, inputOp1(localP, ctx));
		}
	}

	return res;
}