vec3 THIS_apply(in vec3 p, inout ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_indexField
	float i = inputOp_indexField(p, ctx);
	#pragma r:else
	float i = extractIteration(ctx).x;
	#pragma r:endif
	i = mapRange(i, THIS_Indexrange.x, THIS_Indexrange.y, 0., 1.);
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
	vec3 t = mix(THIS_Translate1, THIS_Translate2, i);
	p -= t;
	#pragma r:endif

	#pragma r:if THIS_Enablerotate
	#pragma r:if THIS_Usepivot
	vec3 piv = mix(THIS_Pivot1, THIS_Pivot2, i);
	p -= piv;
	#pragma r:endif
	vec3 r = mix(THIS_Rotate1, THIS_Rotate2, i);
	pRotateOnXYZ(p, r);
	#pragma r:if THIS_Usepivot
	p += piv;
	#pragma r:endif
	#pragma r:endif
	return p;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		p = THIS_asCoordT(THIS_apply(adaptAsVec3(p), ctx));
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}