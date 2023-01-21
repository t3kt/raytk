void THIS_merge(inout Sdf res1, in Sdf res2, CoordT p, ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable)) {
		res = inputOp1(p, ctx);
	} else {
		vec3 q = adaptAsVec3(p);
		vec3 p3 = q;
		float s = THIS_Shift;
		float o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_shiftField
		s += inputOp_shiftField(p, ctx);
		#endif
		#ifdef THIS_HAS_INPUT_offsetField
		o += inputOp_offsetField(p, ctx);
		#endif
		switch (THIS_Axis) {
			case THISTYPE_Axis_x:
				q.x = (q.x + s) * -1. - o;
				p3.x += o - s;
				break;
			case THISTYPE_Axis_y:
				q.y = (q.y + s) * -1. - o;
				p3.y += o - s;
				break;
			case THISTYPE_Axis_z:
				q.z = (q.z + s) * -1. - o;
				p3.z += o - s;
				break;
		}
		int iterB;
		switch (THIS_Iterationtype) {
			case THISTYPE_Iterationtype_sign:
				setIterationIndex(ctx, 1);
				iterB = -1;
				break;
			case THISTYPE_Iterationtype_index:
				setIterationIndex(ctx, 0);
				iterB = 1;
				break;
		}
		#ifdef THIS_EXPOSE_sign
		THIS_sign = 1;
		#endif
		#ifdef THIS_EXPOSE_index
		THIS_index = 0;
		#endif
		#ifndef THIS_RETURN_TYPE_Sdf
		res = inputOp1(THIS_asCoordT(q), ctx);
		#else
		if (int(THIS_Mergetype) == 0) {
			res = inputOp1(THIS_asCoordT(q), ctx);
		} else {
			res = inputOp1(THIS_asCoordT(p3), ctx);
			if (THIS_Iterationtype != THISTYPE_Iterationtype_none) {
				setIterationIndex(ctx, iterB);
			}
			#ifdef THIS_EXPOSE_sign
			THIS_sign = -1;
			#endif
			#ifdef THIS_EXPOSE_index
			THIS_index = 1;
			#endif
			Sdf res2 = inputOp1(THIS_asCoordT(q), ctx);
			THIS_merge(res, res2, THIS_asCoordT(p3), ctx);
		}
		#endif
	}
	return res;
}