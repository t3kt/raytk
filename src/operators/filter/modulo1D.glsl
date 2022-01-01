ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_COORD_TYPE_float
	float q = p;
	#pragma r:else
	float q = p.THIS_Axis;
	#pragma r:endif
	float size = THIS_Size;
	#pragma r:if THIS_HAS_INPUT_sizeField
	{
		#pragma r:if inputOp_sizeField_COORD_TYPE_float
		size *= inputOp_sizeField(q, ctx);
		#pragma r:else
		size *= inputOp_sizeField(p, ctx);
		#pragma r:endif
	}
	#pragma r:endif
	float halfsize = size*0.5;


	float sh = THIS_Shift;
	#pragma r:if THIS_HAS_INPUT_shiftField
	{
		#pragma r:if inputOp_shiftField_COORD_TYPE_float
		float q1 = q;
		#pragma r:else
		inputOp_shiftField_CoordT q1 = inputOp_shiftField_asCoordT(p);
		#pragma r:endif
		sh += inputOp_shiftField(q1, ctx);
	}
	#pragma r:endif
	q += sh;

	float c = floor((q + halfsize)/size);
	q = mod(q+halfsize, size) - halfsize;
	#pragma r:if THIS_Uselimit
	{
		#pragma r:if THIS_Limittype_start || THIS_Limittype_both
		float start = THIS_Limitstart + THIS_Limitoffset;
		if (c < start) applyModLimit(q, c, size, start);
		#pragma r:endif
		#pragma r:if THIS_Limittype_stop || THIS_Limittype_both
		float stop = THIS_Limitstop + THIS_Limitoffset;
		if (c > stop) applyModLimit(q, c, size, stop);
		#pragma r:endif
	}
	#pragma r:endif

	#pragma r:if THIS_Mirrortype_mirror
	q *= mod(c, 2.0)*2 - 1;
	#pragma r:endif

	#pragma r:if THIS_Iterationtype_cellcoord
	setIterationIndex(ctx, c);
	#pragma r:elif THIS_Iterationtype_alternatingcoord
	setIterationIndex(ctx, mod(c, 2.));
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_cellcoord
	THIS_cellcoord = int(c);
	#pragma r:endif

	// offset field can use iteration
	float o = THIS_Offset;
	#pragma r:if THIS_HAS_INPUT_offsetField
	{
		#pragma r:if inputOp_offsetField_COORD_TYPE_float
		float q1 = q;
		#pragma r:else
		inputOp_offsetField_CoordT q1 = inputOp_offsetField_asCoordT(p);
		#pragma r:endif
		o += inputOp_offsetField(q1, ctx);
	}
	#pragma r:endif

	#pragma r:if THIS_COORD_TYPE_float
	p = q - o;
	#pragma r:else
	p.THIS_Axis = q - o;
	#pragma r:endif

	return inputOp1(p, ctx);
}