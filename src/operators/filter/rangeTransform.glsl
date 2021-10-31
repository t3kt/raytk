ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_indexField
	float i = inputOp_indexField(p, ctx);
	#pragma r:else
	float i = extractIteration(ctx).x;
	#pragma r:endif
	i = mapRange(i, THIS_Indexrange1, THIS_Indexrange2, 0., 1.);
	#pragma r:if THIS_Extendmode_linear
	#pragma r:elif THIS_Extendmode_clamp
	i = clamp(i, 0., 1.);
	#pragma r:elif THIS_Extendmode_loop
	i = fract(i);
	#pragma r:else
	#error invalidExtendMode
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_easingFunction
	i = inputOp_easingFunction(i, ctx);
	#pragma r:endif

	#pragma r:if THIS_Enabletranslate
	CoordT t = mix(THIS_Translate1, THIS_Translate2, i);
	p -= t;
	#pragma r:endif

	#pragma r:if THIS_Enablerotate
	#pragma r:if THIS_Usepivot
	CoordT piv = mix(THIS_Pivot1, THIS_Pivot2, i);
	p -= piv;
	#pragma r:endif
	CoordT r = mix(THIS_Rotate1, THIS_Rotate2, i);
	pRotateOnXYZ(p, r);
	#pragma r:if THIS_Usepivot
	p += piv;
	#pragma r:endif
	#pragma r:endif

	return inputOp1(p, ctx);
}