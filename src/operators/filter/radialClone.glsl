void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	#pragma r:if THIS_Iterationtype_index
	setIterationIndex(ctx, i);
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_index
	THIS_index = i;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#pragma r:endif
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res;
	int n = int(THIS_Count);
	float rot = THIS_Angleoffset;
	float angleStep = THIS_Anglerange / THIS_Count;
	CoordT q = p;
#pragma r:if THIS_COORD_TYPE_vec2
	pR(q, rot);
	q.y -= THIS_Radiusoffset;
#pragma r:else
	pR(q.THIS_PLANE, rot);
	q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
#pragma r:endif
	THIS_exposeIndex(ctx, 0, n);
	res = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		rot += angleStep;
		q = p;
		#pragma r:if THIS_COORD_TYPE_vec2
			pR(q, rot);
			q.y -= THIS_Radiusoffset;
		#pragma r:else
			pR(q.THIS_PLANE, rot);
			q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
		#pragma r:endif
		THIS_exposeIndex(ctx, i, n);
		Sdf res2 = inputOp1(q, ctx);
		THIS_combine(res, res2, q, ctx);
	}
	return res;
}