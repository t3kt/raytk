void THIS_apply(inout CoordT p, inout ContextT ctx) {
	vec2 q = getAxisPlane(p, int(THIS_Axis));
	vec2 size = THIS_Size;
	#pragma r:if THIS_HAS_INPUT_sizeField
	{
		#pragma r:if inputOp_sizeField_COORD_TYPE_vec2
		vec2 q1 = q;
		#pragma r:else
		inputOp_sizeField_CoordT q1 = inputOp_sizeField_asCoordT(p);
		#pragma r:endif
		size *= fillToVec2(inputOp_sizeField(q1, ctx));
	}
	#pragma r:endif
	vec2 halfsize = size * 0.5;

	vec2 sh = THIS_Shift;
	#pragma r:if THIS_HAS_INPUT_shiftField
	{
		#pragma r:if inputOp_shiftField_COORD_TYPE_vec2
		vec2 q1 = q;
		#pragma r:else
		inputOp_shiftField_CoordT q1 = inputOp_shiftField_asCoordT(p);
		#pragma r:endif
		sh += fillToVec2(inputOp_shiftField(q1, ctx));
	}
	#pragma r:endif
	q += sh;
	vec2 c = floor((q + halfsize)/size);
	q = mod(q + halfsize, size) - halfsize;
	#pragma r:if THIS_Limittype_both || THIS_Limittype_start
	vec2 start = THIS_Limitstart + THIS_Limitoffset;
	if (c.x < start.x) applyModLimit(q.x, c.x, size.x, start.x);
	if (c.y < start.y) applyModLimit(q.y, c.y, size.y, start.y);
	#pragma r:endif
	#pragma r:if THIS_Limittype_both || THIS_Limittype_stop
	vec2 stop = THIS_Limitstop + THIS_Limitoffset;
	if (c.x > stop.x) applyModLimit(q.x, c.x, size.x, stop.x);
	if (c.y > stop.y) applyModLimit(q.y, c.y, size.y, stop.y);
	#pragma r:endif

	#pragma r:if THIS_Mirrortype_mirror
	q *= mod(c,vec2(2))*2 - vec2(1);
	#pragma r:elif THIS_Mirrortype_grid
	q *= mod(c,vec2(2))*2 - vec2(1);
	q -= halfsize;
	if (q.x > q.y) q.xy = q.yx;
	c = floor(c/2);
	#pragma r:endif

	int quad = quadrantIndex(ivec2(mod(ivec2(c), 2)));
	#pragma r:if THIS_Iterationtype_cellcoord
	setIterationCell(ctx, c);
	#pragma r:elif THIS_Iterationtype_tiledquadrant
	setIterationIndex(ctx, quad);
	#pragma r:elif THIS_Iterationtype_alternatingcoord
	setIterationCell(ctx, mod(c, 2.));
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_cellcoord
	THIS_cellcoord = ivec2(c);
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_tiledquad
	THIS_tiledquad = quad;
	#pragma r:endif
	// offset field can use iteration
	vec2 o = THIS_Offset;
	#pragma r:if THIS_HAS_INPUT_offsetField
	{

		#pragma r:if inputOp_offsetField_COORD_TYPE_vec2
		vec2 q1 = q;
		#pragma r:else
		inputOp_offsetField_CoordT q1 = inputOp_offsetField_asCoordT(p);
		#pragma r:endif
		o += fillToVec2(inputOp_offsetField(q1, ctx));
	}
	#pragma r:endif
	setAxisPlane(p, int(THIS_Axis), q - o);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}