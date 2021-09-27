ReturnT thismap(CoordT p, ContextT ctx) {
	float q = p.THIS_Axis + THIS_Shift;
	float size = THIS_Size;
	float halfsize = size*0.5;
	float c = floor((q + halfsize)/size);
	q = mod(q+halfsize, size) - halfsize;
	#if defined(THIS_Uselimit)
	{
		#if defined(THIS_Limittype_start) || defined(THIS_Limittype_both)
		float start = THIS_Limitstart + THIS_Limitoffset;
		if (c < start) applyModLimit(q, c, size, start);
		#endif
		#if defined(THIS_Limittype_stop) || defined(THIS_Limittype_both)
		float stop = THIS_Limitstop + THIS_Limitoffset;
		if (c > stop) applyModLimit(q, c, size, stop);
		#endif
	}
	#endif

	#ifdef THIS_Mirrortype_mirror
	q *= mod(c, 2.0)*2 - 1;
	#endif

	p.THIS_Axis = q - THIS_Offset;
	#if defined(THIS_Iterationtype_cellcoord)
	setIterationIndex(ctx, c);
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationIndex(ctx, mod(c, 2.));
	#endif
	return inputOp1(p, ctx);
}