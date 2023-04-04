void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	if (THIS_Iterationtype == THISTYPE_Iterationtype_index) {
		setIterationIndex(ctx, i);
	}
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
	#ifdef THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#endif
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Count);
	THIS_exposeIndex(ctx, 0, n);
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	vec3 t1 = THIS_Translate1;
	vec3 t2 = THIS_Translate2;
	vec3 p3 = adaptAsVec3(p);
	Sdf res = inputOp1(THIS_asCoordT(p3 - t1), ctx);
	for (int i = 1; i < n; i++) {
		THIS_exposeIndex(ctx, i, n);
		vec3 t = mix(t1, t2, float(i) / float(n - 1));
		CoordT q = THIS_asCoordT(p3 - t);
		Sdf res2 = inputOp1(q, ctx);
		THIS_combine(res, res2, q, ctx);
	}
	return res;
}