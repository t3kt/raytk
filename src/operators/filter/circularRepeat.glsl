// Circle Repetition SDF by iq
// https://www.shadertoy.com/view/fdVBDw

ReturnT thismap(CoordT p, ContextT ctx) {
	float cs = THIS_Cellsize;
	float ra = THIS_Radius/cs;

	// make grid
	vec2 id0 = round(p/cs);

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
			vec2 q = p - cs*id;

			#ifdef THIS_EXPOSE_cellcoord
			THIS_cellcoord = ivec2(id);
			#endif
			#ifdef THIS_EXPOSE_cellchecker
			THIS_cellchecker = mod(id.x+id.y, 2.) > .5;
			#endif

			res = cmb_simpleUnion(res, inputOp1(q, ctx));
		}
	}

	return res;
}