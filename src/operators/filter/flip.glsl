void THIS_merge(inout Sdf res1, in Sdf res2, CoordT p, ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable)) {
		res = inputOp1(p, ctx);
	} else {
		CoordT q = p;
		float s = THIS_Shift;
		float o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_shiftField
		s += inputOp_shiftField(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx);
		#endif
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
		#if defined(THIS_Iterationtype_sign)
		setIterationIndex(ctx, 1);
		const int iterB = -1;
		#elif defined(THIS_Iterationtype_index)
		setIterationIndex(ctx, 0);
		const int iterB = 1;
		#endif
		#ifdef THIS_EXPOSE_sign
		THIS_sign = 1;
		#endif
		#ifdef THIS_EXPOSE_index
		THIS_index = 0;
		#endif
		if (int(THIS_Mergetype) == 0) {
			res = inputOp1(q, ctx);
		} else {
			res = inputOp1(p, ctx);
			#if !defined(THIS_Iterationtype_none)
			setIterationIndex(ctx, iterB);
			#endif
			#ifdef THIS_EXPOSE_sign
			THIS_sign = -1;
			#endif
			#ifdef THIS_EXPOSE_index
			THIS_index = 1;
			#endif
			Sdf res2 = inputOp1(q, ctx);
			THIS_merge(res, res2, p, ctx);
		}
	}
	return res;
}