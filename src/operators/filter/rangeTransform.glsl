vec3 THIS_apply(in vec3 p, inout ContextT ctx, inout float valueAdjust) {
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

	#ifdef THIS_Enableuniformscale
	float us = mix(THIS_Uniformscale1, THIS_Uniformscale2, i);
	p /= us;
	valueAdjust = us;
	#endif

	#ifdef THIS_Enablescale
	vec3 s = mix(THIS_Scale1, THIS_Scale2, i);
	p /= s;
	#ifdef THIS_COORD_TYPE_float
		valueAdjust *= s.x;
	#else
		valueAdjust *= vmin(s);
	#endif
	#endif

	return p;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.;
	if (IS_TRUE(THIS_Enable)) {
		p = THIS_asCoordT(THIS_apply(adaptAsVec3(p), ctx, valueAdjust));
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, valueAdjust);
	#endif
	return res;
}