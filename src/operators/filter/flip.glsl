void THIS_merge(inout Sdf res1, in Sdf res2, CoordT p, ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (THIS_Enable < 0.5) {
		res = inputOp1(p, ctx);
	} else {
		CoordT q = p;
		switch (int(THIS_Axis)) {
			case 0:
			q.x = (q.x + THIS_Shift) * -1. - THIS_Offset;
			p.x = p.x + THIS_Offset - THIS_Shift;
			break;
			case 1:
			q.y = (q.y + THIS_Shift) * -1. - THIS_Offset;
			p.y = p.y + THIS_Offset - THIS_Shift;
			break;
			#ifdef THIS_COORD_TYPE_vec3
			case 2:
			q.z = (q.z + THIS_Shift) * -1. - THIS_Offset;
			p.z = p.z + THIS_Offset - THIS_Shift;
			break;
			#endif
		}
		#pragma r:if THIS_Iterationtype_sign
		setIterationIndex(ctx, 1);
		const int iterB = -1;
		#pragma r:elif THIS_Iterationtype_index
		setIterationIndex(ctx, 0);
		const int iterB = 1;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_sign
		THIS_sign = 1;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_index
		THIS_index = 0;
		#pragma r:endif
		#pragma r:if THIS_Mergetype_none
		res = inputOp1(q, ctx);
		#pragma r:else
		res = inputOp1(p, ctx);
		#pragma r:if !THIS_Iterationtype_none
		setIterationIndex(ctx, iterB);
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_sign
		THIS_sign = -1;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_index
		THIS_index = 1;
		#pragma r:endif
		Sdf res2 = inputOp1(q, ctx);
		THIS_merge(res, res2, p, ctx);
		#pragma r:endif
	}
	return res;
}