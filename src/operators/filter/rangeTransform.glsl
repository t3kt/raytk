vec3 THIS_apply(in vec3 p, inout ContextT ctx) {
	#ifdef THIS_HAS_INPUT_indexField
	float i = inputOp_indexField(p, ctx);
	#else
	float i = extractIteration(ctx).x;
	#endif
	i = mapRange(i, THIS_Indexrange.x, THIS_Indexrange.y, 0., 1.);
	#if defined(THIS_Extendmode_linear)
	#elif defined(THIS_Extendmode_clamp)
	i = clamp(i, 0., 1.);
	#elif defined(THIS_Extendmode_loop)
	i = fract(i);
	#else
	#error invalidExtendMode
	#endif
	#ifdef THIS_HAS_INPUT_easingFunction
	i = inputOp_easingFunction(i, ctx);
	#endif

	#ifdef THIS_Enabletranslate
	vec3 t = mix(THIS_Translate1, THIS_Translate2, i);
	p -= t;
	#endif

	#ifdef THIS_Enablerotate
	#ifdef THIS_Usepivot
	vec3 piv = mix(THIS_Pivot1, THIS_Pivot2, i);
	p -= piv;
	#endif
	vec3 r = mix(THIS_Rotate1, THIS_Rotate2, i);
	pRotateOnXYZ(p, r);
	#ifdef THIS_Usepivot
	p += piv;
	#endif
	#endif
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