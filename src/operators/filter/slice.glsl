ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (THIS_Enable >= 0.5) {
		float q;
		switch (int(THIS_Axis)) {
			case 0: q = p.x; break;
			case 1: q = p.y; break;
			case 2: q = p.z; break;
		}
		if (IS_TRUE(THIS_Enablemirror)) {
			q = abs(q);
		}
		#pragma r:if THIS_HAS_INPUT_offsetField
		float o = inputOp_offsetField(p, ctx);
		#pragma r:else
		float o = THIS_Offset;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_thicknessField
		float th = inputOp_thicknessField(p, ctx);
		#pragma r:else
		float th = THIS_Thickness;
		#pragma r:endif
		float d = abs(q - o) - th;
		#pragma r:if THIS_Operation_intersect
		#pragma r:elif THIS_Operation_diff
		{
			d = -d;
		}
		#pragma r:else
		#error invalidOperation
		#pragma r:endif
		if (IS_TRUE(THIS_Enablesmoothing)) {
			res.x = fOpIntersectionRound(res.x, d, THIS_Smoothradius);
		} else {
			res.x = max(res.x, d);
		}
	}
	return res;
}