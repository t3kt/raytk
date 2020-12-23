ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p;
	q.THIS_AXIS += THIS_Shift;
	q.THIS_AXIS *= -1;
	q.THIS_AXIS -= THIS_Offset;
	p.THIS_AXIS += THIS_Offset;
	p.THIS_AXIS -= THIS_Shift;
	#if defined(THIS_Mergetype_none)
		#ifdef THIS_Iterateonsides
		ctx.iteration = vec4(1, 2, 0, 0);
		#endif
		return inputOp1(q, ctx);
	#else
		#ifdef THIS_Iterateonsides
		ctx.iteration = vec4(0, 2, 0, 0);
		#endif
		Sdf res1 = inputOp1(p, ctx);
		#ifdef THIS_Iterateonsides
		ctx.iteration.x = 1;
		#endif
		Sdf res2 = inputOp1(q, ctx);
		#ifdef THIS_Mergetype_smoothUnion
			return opSmoothUnionM(res1, res2, THIS_Mergeradius);
		#else
			return opSimpleUnion(res1, res2);
		#endif
	#endif
}