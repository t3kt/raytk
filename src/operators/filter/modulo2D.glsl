void THIS_apply(inout CoordT p, inout ContextT ctx) {
	vec2 q = getAxisPlane(p, int(THIS_Axis));
	vec2 size = THIS_Size;
	#ifdef THIS_HAS_INPUT_sizeField
	{
		#ifdef inputOp_sizeField_COORD_TYPE_vec2
		vec2 q1 = q;
		#else
		inputOp_sizeField_CoordT q1 = inputOp_sizeField_asCoordT(p);
		#endif
		size *= fillToVec2(inputOp_sizeField(q1, ctx));
	}
	#endif
	vec2 halfsize = size * 0.5;

	vec2 sh = THIS_Shift;
	#ifdef THIS_HAS_INPUT_shiftField
	{
		#ifdef inputOp_shiftField_COORD_TYPE_vec2
		vec2 q1 = q;
		#else
		inputOp_shiftField_CoordT q1 = inputOp_shiftField_asCoordT(p);
		#endif
		sh += fillToVec2(inputOp_shiftField(q1, ctx));
	}
	#endif
	q += sh;
	vec2 c = floor((q + halfsize)/size);
	q = mod(q + halfsize, size) - halfsize;
	vec2 start, stop;
	if (int(THIS_Limittype) == THISTYPE_Limittype_start || int(THIS_Limittype) == THISTYPE_Limittype_both) {
		start = THIS_Limitstart + THIS_Limitoffset;
		if (c.x < start.x) applyModLimit(q.x, c.x, size.x, start.x);
		if (c.y < start.y) applyModLimit(q.y, c.y, size.y, start.y);
	}
	if (int(THIS_Limittype) == THISTYPE_Limittype_stop || int(THIS_Limittype) == THISTYPE_Limittype_both) {
		stop = THIS_Limitstop + THIS_Limitoffset;
		if (c.x > stop.x) applyModLimit(q.x, c.x, size.x, stop.x);
		if (c.y > stop.y) applyModLimit(q.y, c.y, size.y, stop.y);
	}

	switch (int(THIS_Mirrortype)) {
		case THISTYPE_Mirrortype_mirror:
			q *= mod(c,vec2(2))*2 - vec2(1);
			break;
		case THISTYPE_Mirrortype_grid:
			q *= mod(c,vec2(2))*2 - vec2(1);
			q -= halfsize;
			if (q.x > q.y) q.xy = q.yx;
			c = floor(c/2);
			break;
	}

	int quad = quadrantIndex(ivec2(mod(ivec2(c), 2)));
	switch (int(THIS_Iterationtype)) {
		case THISTYPE_Iterationtype_cellcoord:
			setIterationCell(ctx, c);
			break;
		case THISTYPE_Iterationtype_tiledquadrant:
			setIterationIndex(ctx, quad);
			break;
		case THISTYPE_Iterationtype_alternatingcoord:
			setIterationCell(ctx, mod(c, 2.));
			break;
	}
	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = ivec2(c);
	#endif
	#ifdef THIS_EXPOSE_tiledquad
	THIS_tiledquad = quad;
	#endif
	#ifdef THIS_EXPOSE_normcoord
	{
		switch (int(THIS_Limittype)) {
			case THISTYPE_Limittype_none:
				THIS_normcoord = c;
				break;
			case THISTYPE_Limittype_start:
				THIS_normcoord = c - start;
				break;
			case THISTYPE_Limittype_stop:
				THIS_normcoord = -c + stop;
				break;
			case THISTYPE_Limittype_both:
				THIS_normcoord = map01(c, start, stop);
				break;
		}
	}
	#endif
	#ifdef THIS_EXPOSE_shiftedcellcoord
	THIS_shiftedcellcoord = c - sh;
	#endif
	// offset field can use iteration
	vec2 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	{
		#ifdef inputOp_offsetField_COORD_TYPE_vec2
		vec2 q1 = q;
		#else
		inputOp_offsetField_CoordT q1 = inputOp_offsetField_asCoordT(p);
		#endif
		o += fillToVec2(inputOp_offsetField(q1, ctx));
	}
	#endif
	setAxisPlane(p, int(THIS_Axis), q - o);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}