ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 pivot = THIS_Pivot;
	vec2 q = p.THIS_PLANE;
	q -= pivot;
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_rotateField
	r += radians(inputOp_rotateField(p, ctx));
	#endif
	pR(q, r);
	float cell = THIS_EXPR;
	float pr = THIS_Prerotate;
	#ifdef THIS_HAS_INPUT_preRotateField
	pr += radians(inputOp_preRotateField(p, ctx));
	#endif
	pR(q, pr);
	vec2 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += inputOp_offsetField(p, ctx).xy;
	#endif
	p.THIS_PLANE = q - o + pivot;
	#if defined(THIS_Iterationtype_index)
	setIterationIndex(ctx, cell);
	#elif defined(THIS_Iterationtype_ratio)
	setIterationIndex(ctx, cell / (THIS_Repetitions - 1.));
	#endif
	return inputOp1(p, ctx);
}