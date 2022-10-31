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
	Sdf res;
	float rot = THIS_Angleoffset;
	float angleStep = THIS_Anglerange / THIS_Count;
	CoordT q = p;
#ifdef THIS_COORD_TYPE_vec2
	pR(q, rot);
	q.y -= THIS_Radiusoffset;
#else
	pR(q.THIS_PLANE, rot);
	q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
#endif
	res = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		rot += angleStep;
		q = p;
		#ifdef THIS_COORD_TYPE_vec2
			pR(q, rot);
			q.y -= THIS_Radiusoffset;
		#else
			pR(q.THIS_PLANE, rot);
			q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
		#endif
		THIS_exposeIndex(ctx, i, n);
		Sdf res2 = inputOp1(q, ctx);
		THIS_combine(res, res2, q, ctx);
	}
	return res;
}