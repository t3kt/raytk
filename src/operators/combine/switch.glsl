float THIS_applyExtend(float i, float n) {
	EXTEND();
	return i;
}

ReturnT THIS_getInput(float source, int n, CoordT p, ContextT ctx) {
	ReturnT res;
	initDefVal(res);
	int i = int(THIS_applyExtend(source, n)) + 1;
	switch (i) {
		AGGREGATE_BODY();
	}
	return res;
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
		#ifndef THIS_Blend
		res = THIS_getInput(source, n, p, ctx);
		#else
		float source1 = floor(source);
		float source2 = ceil(source);
		res = THIS_getInput(source1, n, p, ctx);
		if (source1 != source2) {
			ReturnT res2 = THIS_getInput(source2, n, p, ctx);
			res = mixVals(res, res2, fract(source));
		}
		#endif
	#endif
	return res;
}