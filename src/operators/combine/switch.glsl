float THIS_applyExtend(float i, float n) {
	EXTEND();
	return i;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if THIS_INPUT_COUNT == 0
	initDefVal(res);
	#else
		#ifdef THIS_HAS_INPUT_indexField
		float source = inputOp_indexField(p, ctx);
		#else
		float source = THIS_Source;
		#endif
		int n = int(THIS_lastInput);
		RESCALEINDEX();
		int i = int(THIS_applyExtend(source, n)) + 1;
		initDefVal(res);
		switch (i) {
			AGGREGATE_BODY();
		}
	#endif
	return res;
}