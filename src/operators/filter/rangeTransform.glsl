ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_2
	float i = inputOp2(p, ctx);
	#else
	float i = extractIteration(ctx).x;
	#endif
	i = mapRange(i, THIS_Indexrange1, THIS_Indexrange2, 0., 1.);
	#if defined(THIS_Extendmode_linear)
	#elif defined(THIS_Extendmode_clamp)
	i = clamp(i, 0., 1.);
	#elif defined(THIS_Extendmode_loop)
	i = fract(i);
	#else
	#error invalidExtendMode
	#endif
	#ifdef THIS_HAS_INPUT_3
	i = inputOp3(i, ctx);
	#endif

	#ifdef THIS_Enabletranslate
	CoordT t = mix(THIS_Translate1, THIS_Translate2, i);
	p -= t;
	#endif

	#ifdef THIS_Enablerotate
	#ifdef THIS_Usepivot
	CoordT piv = mix(THIS_Pivot1, THIS_Pivot2, i);
	p -= piv;
	#endif
	CoordT r = mix(THIS_Rotate1, THIS_Rotate2, i);
	pRotateOnXYZ(p, r);
	#ifdef THIS_Usepivot
	p += piv;
	#endif
	#endif

	return inputOp1(p, ctx);
}