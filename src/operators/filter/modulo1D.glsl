void THIS_apply(inout CoordT p, inout ContextT ctx) {
	#ifdef THIS_COORD_TYPE_float
	float q = p;
	#else
	float q = getAxis(p, int(THIS_Axis));
	#endif
	float size = THIS_Size;
	#ifdef THIS_HAS_INPUT_sizeField
	{
		#ifdef inputOp_sizeField_COORD_TYPE_float
		size *= inputOp_sizeField(q, ctx);
		#else
		size *= inputOp_sizeField(p, ctx);
		#endif
	}
	#endif
	float halfsize = size*0.5;


	float sh = THIS_Shift;
	#ifdef THIS_HAS_INPUT_shiftField
	{
		#ifdef inputOp_shiftField_COORD_TYPE_float
		float q1 = q;
		#else
		inputOp_shiftField_CoordT q1 = inputOp_shiftField_asCoordT(p);
		#endif
		sh += inputOp_shiftField(q1, ctx);
	}
	#endif
	q += sh;

	float c = floor((q + halfsize)/size);
	q = mod(q+halfsize, size) - halfsize;
	float start, stop;
	#ifdef THIS_Uselimit
	{
		#if defined(THIS_Limittype_start) || defined(THIS_Limittype_both)
		start = THIS_Limitstart + THIS_Limitoffset;
		if (c < start) applyModLimit(q, c, size, start);
		#endif
		#if defined(THIS_Limittype_stop) || defined(THIS_Limittype_both)
		stop = THIS_Limitstop + THIS_Limitoffset;
		if (c > stop) applyModLimit(q, c, size, stop);
		#endif
	}
	#endif

	#ifdef THIS_Mirrortype_mirror
	q *= mod(c, 2.0)*2 - 1;
	#endif

	#if defined(THIS_Iterationtype_cellcoord)
	setIterationIndex(ctx, c);
	#elif defined(THIS_Iterationtype_alternatingcoord)
	setIterationIndex(ctx, mod(c, 2.));
	#endif
	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = int(c);
	#endif
	#ifdef THIS_EXPOSE_normcoord
	{
		#if !defined(THIS_Uselimit)
		THIS_normcoord = c;
		#elif defined(THIS_Limittype_start)
		THIS_normcoord = c - start;
		#elif defined(THIS_Limittype_stop)
		THIS_normcoord = -c + stop;
		#elif defined(THIS_Limittype_both)
		THIS_normcoord = map01(c, start, stop);
		#endif
	}
	#endif

	// offset field can use iteration
	float o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	{
		#ifdef inputOp_offsetField_COORD_TYPE_float
		float q1 = q;
		#else
		inputOp_offsetField_CoordT q1 = inputOp_offsetField_asCoordT(p);
		#endif
		o += inputOp_offsetField(q1, ctx);
	}
	#endif

	#ifdef THIS_COORD_TYPE_float
	p = q - o;
	#else
	setAxis(p, int(THIS_Axis), q - o);
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		THIS_apply(p, ctx);
	}
	return inputOp1(p, ctx);
}