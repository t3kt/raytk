ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p + THIS_Shift;
	vec3 size = THIS_Size;
	vec3 halfsize = size * 0.5;

	vec3 c = floor((q + halfsize) / size);
	q = mod(q + halfsize, size) - halfsize;

	#if defined(THIS_Limittype_both) || defined(THIS_Limittype_start)
	vec3 start = THIS_Limitstart + THIS_Limitoffset;
	if (c.x < start.x) applyModLimit(q.x, c.x, size.x, start.x);
	if (c.y < start.y) applyModLimit(q.y, c.y, size.y, start.y);
	if (c.z > start.z) applyModLimit(q.z, c.z, size.z, start.z);
	#endif
	#if defined(THIS_Limittype_both) || defined(THIS_Limittype_stop)
	vec3 stop = THIS_Limitstop + THIS_Limitoffset;
	if (c.x > stop.x) applyModLimit(q.x, c.x, size.x, stop.x);
	if (c.y > stop.y) applyModLimit(q.y, c.y, size.y, stop.y);
	if (c.z > stop.z) applyModLimit(q.z, c.z, size.z, stop.z);
	#endif

	#if defined(THIS_Mirrortype_mirror)
	q *= mod(c, vec3(2.))*2. - vec3(1.);
	#endif

	p = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationCell(ctx, c);
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationCell(ctx, mod(c, 2.));
	#endif
	return inputOp1(p, ctx);
}