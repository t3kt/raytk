void THIS_merge(inout ReturnT res1, in ReturnT res2, float r, float n, float o) {
MERGE_BODY();
}

void THIS_exposeIndex(int i) {
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	MERGE_PREP();
	ReturnT res1 = createNonHitSdf();
	MERGE_DEFAULT_INIT();
	CoordT p1 = p;
	AGGREGATE_BODY();
	MERGE_POST_PROC();
	return res1;
}