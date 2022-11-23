void THIS_apply(inout CoordT p, inout ContextT ctx) {
	vec3 q = p;
	vec3 size = THIS_Size;
	#ifdef THIS_HAS_INPUT_sizeField
	size *= fillToVec3(inputOp_sizeField(p, ctx));
	#endif
	vec3 halfsize = size * 0.5;

	vec3 sh = THIS_Shift;
	#ifdef THIS_HAS_INPUT_shiftField
	sh += fillToVec3(inputOp_shiftField(p, ctx));
	#endif
	q += sh;
	vec3 c = floor((q + halfsize) / size);
	q = mod(q + halfsize, size) - halfsize;

	vec3 start, stop;
	if (THIS_Limittype == THISTYPE_Limittype_start || THIS_Limittype == THISTYPE_Limittype_both) {
		start = THIS_Limitstart + THIS_Limitoffset;
		if (c.x < start.x) applyModLimit(q.x, c.x, size.x, start.x);
		if (c.y < start.y) applyModLimit(q.y, c.y, size.y, start.y);
		if (c.z < start.z) applyModLimit(q.z, c.z, size.z, start.z);
	}
	if (THIS_Limittype == THISTYPE_Limittype_stop || THIS_Limittype == THISTYPE_Limittype_both) {
		stop = THIS_Limitstop + THIS_Limitoffset;
		if (c.x > stop.x) applyModLimit(q.x, c.x, size.x, stop.x);
		if (c.y > stop.y) applyModLimit(q.y, c.y, size.y, stop.y);
		if (c.z > stop.z) applyModLimit(q.z, c.z, size.z, stop.z);
	}

	if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
		q *= mod(c, vec3(2.))*2. - vec3(1.);
	}

	switch (THIS_Iterationtype) {
		case THISTYPE_Iterationtype_cellcoord:
			setIterationCell(ctx, c);
			break;
		case THISTYPE_Iterationtype_alternatingcoord:
			setIterationCell(ctx, mod(c, 2.));
			break;
	}
	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = ivec3(c);
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

	// offset field can use iteration
	vec3 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += fillToVec3(inputOp_offsetField(p, ctx));
	#endif
	p = q - o;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}