// https://www.osar.fr/notes/logspherical/

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_vec2
	vec2 q = p;
	#else
		vec2 q;
		switch (THIS_Axis) {
			case THISTYPE_Axis_x: q = p.yz; break;
			case THISTYPE_Axis_y: q = p.zx; break;
			case THISTYPE_Axis_z: q = p.xy; break;
		}
	#endif

	float scale = THIS_Radialreps/TAU;
	float scaleAdj = 1.0;
	vec2 cell = vec2(0.);
	vec2 size = vec2(THIS_Distspacing, 1.);

	#if defined(THIS_Mode_logpolar)
	float r = length(q);
	q = vec2(log(r), atan(q.y, q.x));
	q -= vec2(THIS_Rhooffset, THIS_Thetaoffset);
	q.y *= scale;
	scaleAdj = r / scale;
	#endif
	switch (THIS_Mirrortype) {
		case THISTYPE_Mirrortype_none:
			cell = pMod2(q, size);
			break;
		case THISTYPE_Mirrortype_mirror:
			cell = pModMirror2(q, size);
			break;
		case THISTYPE_Mirrortype_grid:
			cell = pModGrid2(q, size);
			break;
	}

	if (THIS_Iterationtype == THISTYPE_Iterationtype_cellcoord) {
		setIterationCell(ctx, cell);
	}

	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = ivec2(cell);
	#endif

	#ifdef THIS_COORD_TYPE_vec2
	p = q;
	#else
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: p.yz = q; p.x /= scaleAdj; break;
		case THISTYPE_Axis_y: p.zx = q; p.y /= scaleAdj; break;
		case THISTYPE_Axis_z: p.xy = q; p.z /= scaleAdj; break;
	}
	#endif
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, scaleAdj);
	#endif
	return res;
}