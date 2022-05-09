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
	CoordT p1 = p;
	AGGREGATE_BODY();
	return res1;
}