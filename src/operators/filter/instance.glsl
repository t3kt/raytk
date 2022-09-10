CoordT THIS_transform(CoordT p, int i) {
	#pragma r:if THIS_HAS_TRANSLATE
	p -= THIS_asCoordT(THIS_translates[i]);
	#pragma r:endif
	#pragma r:if THIS_HAS_ROTATE
	#pragma r:if THIS_COORD_TYPE_vec3
	pRotateOnXYZ(p, radians(THIS_rotates[i]));
	#pragma r:elif THIS_COORD_TYPE_vec2
	pR(p, radians(THIS_rotates[i].z));
	#pragma r:endif
	#pragma r:endif
	return p;
}

void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	setIterationIndex(ctx, i);
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
	ReturnT res;
	if (IS_FALSE(THIS_Enable)) {
		THIS_exposeIndex(ctx, 0, 1);
		res = inputOp1(p, ctx);
	} else {
		int n = int(THIS_Instancecount);
		THIS_exposeIndex(ctx, 0, n);
		CoordT q = THIS_transform(p, 0);
		res = inputOp1(q, ctx);
		for (int i = 1; i < n; i++) {
			THIS_exposeIndex(ctx, i, n);
			q = THIS_transform(p, i);
			ReturnT res2 = inputOp1(q, ctx);
			THIS_combine(res, res2, q, ctx);
		}
	}
	return res;
}
