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
	if (IS_TRUE(THIS_Uselimit)) {
		if (THIS_Limittype == THISTYPE_Limittype_start || THIS_Limittype == THISTYPE_Limittype_both) {
			start = THIS_Limitstart + THIS_Limitoffset;
			if (c < start) applyModLimit(q, c, size, start);
		}
		if (THIS_Limittype == THISTYPE_Limittype_stop || THIS_Limittype == THISTYPE_Limittype_both) {
			stop = THIS_Limitstop + THIS_Limitoffset;
			if (c > stop) applyModLimit(q, c, size, stop);
		}
	}

	if (THIS_Mirrortype == THISTYPE_Mirrortype_mirror) {
		q *= mod(c, 2.0)*2 - 1;
	}

	switch (THIS_Iterationtype) {
		case THISTYPE_Iterationtype_cellcoord:
			setIterationIndex(ctx, c);
			break;
		case THISTYPE_Iterationtype_alternatingcoord:
			setIterationIndex(ctx, mod(c, 2.));
			break;
	}
	#ifdef THIS_EXPOSE_cellcoord
	THIS_cellcoord = int(c);
	#endif
	#ifdef THIS_EXPOSE_normcoord
	{
		if (IS_FALSE(THIS_Uselimit)) {
			THIS_normcoord = c;
		} else if (THIS_Limittype == THISTYPE_Limittype_start) {
			THIS_normcoord = c - start;
		} else if (THIS_Limittype == THISTYPE_Limittype_stop) {
			THIS_normcoord = -c + stop;
		} else if (THIS_Limittype == THISTYPE_Limittype_both) {
			THIS_normcoord = map01(c, start, stop);
		}
	}
	#endif
	#ifdef THIS_EXPOSE_shiftedcellcoord
	THIS_shiftedcellcoord = c - sh * 0.5;
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