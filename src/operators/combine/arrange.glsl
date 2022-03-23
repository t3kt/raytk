void THIS_merge(inout ReturnT res1, in ReturnT res2, float r, float n, float o) {
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	MERGE_PREP();
	ReturnT res1 = createNonHitSdf();
	AGGREGATE_BODY();
	return res1;
}