ReturnT thismap(CoordT p, ContextT ctx) {
	float i = mapRange(ctx.iteration.x, THIS_Indexrange1, THIS_Indexrange2, 0., 1.);
	#if defined(THIS_Extendmode_linear)
	#elif defined(THIS_Extendmode_clamp)
	i = clamp(i, 0., 1.);
	#elif defined(THIS_Extendmode_loop)
	i = fract(i);
	#else
	#error invalidExtendMode
	#endif

	#ifdef THIS_Enabletranslate
	CoordT t = mix(THIS_Translate1, THIS_Translate2, i);
	p -= t;
	#endif

	#ifdef THIS_Enablerotate
	CoordT r = mix(THIS_Rotate1, THIS_Rotate2, i);
	pRotateOnXYZ(p, r);
	#endif

	return inputOp1(p, ctx);
}