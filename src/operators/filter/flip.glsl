ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p;
	q.THIS_AXIS += THIS_Shift;
	q.THIS_AXIS *= -1;
	q.THIS_AXIS -= THIS_Offset;
	p.THIS_AXIS += THIS_Offset;
	p.THIS_AXIS -= THIS_Shift;
	#if defined(THIS_Iterationtype_sign)
	setIterationIndex(ctx, 1);
	const int iterB = -1;
	#elif defined(THIS_Iterationtype_index)
	setIterationIndex(ctx, 0);
	const int iterB = 1;
	#endif
	#if defined(THIS_Mergetype_none)
		return inputOp1(q, ctx);
	#else
		Sdf res1 = inputOp1(p, ctx);
		#ifndef THIS_Iterationtype_none
		setIterationIndex(ctx, iterB);
		#endif
		Sdf res2 = inputOp1(q, ctx);
		#ifdef THIS_Mergetype_smoothUnion
			return opSmoothUnionM(res1, res2, THIS_Mergeradius);
		#else
			return opSimpleUnion(res1, res2);
		#endif
	#endif
}