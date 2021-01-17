ReturnT thismap(float p, ContextT ctx) {
	#if THIS_INPUT_COUNT == 0
		return 0.;
	#elif THIS_INPUT_COUNT == 1
		return THIS_INPUT_1(p, ctx);
	#else
		float n = float(THIS_INPUT_COUNT);
		float i = p * n;

		if (i <= 1.) {
			return THIS_INPUT_1(i, ctx);
		}
		if (i <= 2.) {
			return THIS_INPUT_2(i - 1., ctx);
		}
		#if THIS_INPUT_COUNT > 2
			if (i <= 3.) {
			return THIS_INPUT_3(i - 2., ctx);
		}
		#endif
		#if THIS_INPUT_COUNT > 3
		return THIS_INPUT_3(i - 4., ctx);
		#endif
		return 0.;
	#endif
}