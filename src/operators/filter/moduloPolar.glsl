ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_4
	r += radians(inputOp4(p, ctx));
	#endif
	pR(q, r);
	float cell = THIS_EXPR;
	float pr = THIS_Prerotate;
	#ifdef THIS_HAS_INPUT_2
	pr += radians(inputOp2(p, ctx));
	#endif
	pR(q, pr);
	vec2 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_3
	o += inputOp3(p, ctx).xy;
	#endif
	p.THIS_PLANE = q - o;
	#if defined(THIS_Iterationtype_index)
	setIterationIndex(ctx, cell);
	#elif defined(THIS_Iterationtype_ratio)
	setIterationIndex(ctx, cell / (THIS_Repetitions - 1.));
	#endif
	return inputOp1(p, ctx);
}