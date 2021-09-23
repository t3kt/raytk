ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE + THIS_Shift;
	vec2 size = THIS_Size;
	vec2 halfsize = size * 0.5;

	vec2 c = floor((q + halfsize)/size);
	q = mod(q + halfsize, size) - halfsize;
	#if defined(THIS_Limittype_both) || defined(THIS_Limittype_start)
	vec2 start = THIS_Limitstart + THIS_Limitoffset;
	if (c.x < start.x) applyModLimit(q.x, c.x, size.x, start.x);
	if (c.y < start.y) applyModLimit(q.y, c.y, size.y, start.y);
	#endif
	#if defined(THIS_Limittype_both) || defined(THIS_Limittype_stop)
	vec2 stop = THIS_Limitstop + THIS_Limitoffset;
	if (c.x > stop.x) applyModLimit(q.x, c.x, size.x, stop.x);
	if (c.y > stop.y) applyModLimit(q.y, c.y, size.y, stop.y);
	#endif

	#if defined(THIS_Mirrortype_mirror)
	q *= mod(c,vec2(2))*2 - vec2(1);
	#elif defined(THIS_Mirrortype_grid)
	q *= mod(c,vec2(2))*2 - vec2(1);
	q -= halfsize;
	if (q.x > q.y) q.xy = q.yx;
	c = floor(c/2);
	#endif

	p.THIS_PLANE = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationCell(ctx, c);
	#elif defined(THIS_Iterationtype_tiledquadrant)
	setIterationIndex(ctx, quadrantIndex(ivec2(mod(ivec2(c), 2))));
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationCell(ctx, mod(c, 2.));
	#endif
	return inputOp1(p, ctx);
}