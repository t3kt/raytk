void THIS_merge(
	int mode, inout ReturnT res1, in ReturnT res2,
	float r, float n, float o) {
	MERGE_BODY();
}

void THIS_defaultInit(
	int mode, out ReturnT res1) {
	MERGE_DEFAULT_INIT();
}

ReturnT THIS_getInput(int i, CoordT p, ContextT ctx) {
	switch (i) {
		#ifdef THIS_HAS_INPUT_1
		case 0: return inputOp1(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_2
		case 1: return inputOp2(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_3
		case 2: return inputOp3(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_4
		case 3: return inputOp4(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_5
		case 4: return inputOp5(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_6
		case 5: return inputOp6(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_7
		case 6: return inputOp7(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_8
		case 7: return inputOp8(p, ctx);
		#endif
	}
	return createNonHitSdf();
}

void THIS_exposeIndex(int i) {
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
}

void THIS_processStep(
	int step, inout ReturnT res, inout bool initialized,
	int mode, float r, float n,  float o, int inNum,
	CoordT p, ContextT ctx) {
	THIS_exposeIndex(step);
	ReturnT res2 = THIS_getInput(inNum, p, ctx);
	if (!initialized) {
		res = res2;
		initialized = true;
	} else {
		THIS_merge(mode, res, res2, r, n, o);
	}
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = createNonHitSdf();
	bool initialized = false;
	AGGREGATE_BODY();
	return res;
}