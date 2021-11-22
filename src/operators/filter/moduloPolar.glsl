ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 pivot = THIS_Pivot;
	vec2 q = p.THIS_PLANE;
	q -= pivot;
	float r = THIS_Rotate;
	#pragma r:if THIS_HAS_INPUT_rotateField
	r += radians(inputOp_rotateField(p, ctx));
	#pragma r:endif
	pR(q, r);
	float cell = THIS_EXPR;
	#pragma r:if THIS_Iterationtype_index
	setIterationIndex(ctx, cell);
	#pragma r:elif THIS_Iterationtype_ratio
	setIterationIndex(ctx, cell / (THIS_Repetitions - 1.));
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_step
	THIS_step = cell;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normstep
	THIS_normstep = cell / (THIS_Repetitions - 1.);
	#pragma r:endif
	float pr = THIS_Prerotate;
	#pragma r:if THIS_HAS_INPUT_preRotateField
	pr += radians(inputOp_preRotateField(p, ctx));
	#pragma r:endif
	pR(q, pr);
	vec2 o = THIS_Offset;
	#pragma r:if THIS_HAS_INPUT_offsetField
	o += inputOp_offsetField(p, ctx).xy;
	#pragma r:endif
	p.THIS_PLANE = q - o + pivot;
	return inputOp1(p, ctx);
}