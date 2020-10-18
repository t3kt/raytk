ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p;
	q.THIS_AXIS += THIS_Shift;
	q.THIS_AXIS *= -1;
	q.THIS_AXIS -= THIS_Offset;
	p.THIS_AXIS += THIS_Offset;
	p.THIS_AXIS -= THIS_Shift;
	#if defined(THIS_MERGE_none)
		#ifdef THIS_ITERATE_SIDES
		ctx.iteration = vec4(1, 2, 0, 0);
		#endif
		return inputOp1(q, ctx);
	#else
		#ifdef THIS_ITERATE_SIDES
		ctx.iteration = vec4(0, 2, 0, 0);
		#endif
		Sdf res1 = inputOp1(p, ctx);
		#ifdef THIS_ITERATE_SIDES
		ctx.iteration.x = 1;
		#endif
		Sdf res2 = inputOp1(q, ctx);
		#ifdef THIS_MERGE_smoothUnion
			return opSmoothUnionM(res1, res2, THIS_Mergeradius);
		#else
			return opSimpleUnion(res1, res2);
		#endif
	#endif
}