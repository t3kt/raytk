void THIS_transformStep(inout vec4 q, CoordT p, inout ContextT ctx) {
	BODY();
}

void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return; }
	#ifdef THIS_Enableloop
	int n = int(THIS_Iterations);
	for (int i = 0; i < n; i++) {
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#endif
		THIS_transformStep(q, p, ctx);
	}
	#else
	THIS_transformStep(q, p, ctx);
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_step
	THIS_step = 0;
	#endif
	#ifdef THIS_EXPOSE_normstep
	THIS_normstep = 0;
	#endif
	ReturnT res;
	APPLY_TO_TARGET();
	return res;
}