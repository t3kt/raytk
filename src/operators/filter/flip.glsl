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
		float s = THIS_Shift;
		float o = THIS_Offset;
		#pragma r:if THIS_HAS_INPUT_shiftField
		s += inputOp_shiftField(p, ctx);
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx);
		#pragma r:endif
		switch (int(THIS_Axis)) {
			case 0:
			q.x = (q.x + s) * -1. - o;
			p.x = p.x + o - s;
			break;
			case 1:
			q.y = (q.y + s) * -1. - o;
			p.y = p.y + o - s;
			break;
			#ifdef THIS_COORD_TYPE_vec3
			case 2:
			q.z = (q.z + s) * -1. - o;
			p.z = p.z + o - s;
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
		if (int(THIS_Mergetype) == 0) {
			res = inputOp1(q, ctx);
		} else {
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
		}
	}
	return res;
}