ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_COORD_TYPE_float
	float q = p + THIS_Shift;
	#pragma r:else
	float q = p.THIS_Axis + THIS_Shift;
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

	#pragma r:if THIS_COORD_TYPE_float
	p = q - THIS_Offset;
	#pragma r:else
	p.THIS_Axis = q - THIS_Offset;
	#pragma r:endif
	#pragma r:if THIS_Iterationtype_cellcoord
	setIterationIndex(ctx, c);
	#pragma r:elif THIS_Iterationtype_alternatingcoord
	setIterationIndex(ctx, mod(c, 2.));
	#pragma r:endif
	return inputOp1(p, ctx);
}