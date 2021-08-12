ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	p = THIS_asCoordT(inputOp1(p, ctx));
	#endif
	THIS_NOISE_COORD_TYPE q;
	#if defined(THIS_COORD_TYPE_vec2)
		q = THIS_asNoiseCoordT(p);
	#elif defined(THIS_COORD_TYPE_vec3)
		#if defined(THIS_NOISE_COORD_vec2)
		q = p.THIS_PLANE;
		#else
		q = THIS_asNoiseCoordT(p);
		#endif
	#endif
	q -= THIS_asNoiseCoordT(THIS_Translate);
	q /= THIS_asNoiseCoordT(THIS_Scale);

	ReturnT val = THIS_FUNCTION(q);
	return (val * THIS_Amplitude) + THIS_Offset;
}