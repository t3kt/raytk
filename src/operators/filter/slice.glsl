ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		float q;
		switch (int(THIS_Axis)) {
			case 0: q = p.x; break;
			case 1: q = p.y; break;
			case 2: q = p.z; break;
		}
		if (IS_TRUE(THIS_Enablemirror)) {
			q = abs(q);
		}
		#ifdef THIS_HAS_INPUT_offsetField
		float o = inputOp_offsetField(p, ctx);
		#else
		float o = THIS_Offset;
		#endif
		#ifdef THIS_HAS_INPUT_thicknessField
		float th = inputOp_thicknessField(p, ctx);
		#else
		float th = THIS_Thickness;
		#endif
		float d = abs(q - o) - th;
		#if defined(THIS_Operation_intersect)
		#elif defined(THIS_Operation_diff)
		d = -d;
		#else
		#error invalidOperation
		#endif
		if (IS_TRUE(THIS_Enablesmoothing)) {
			res.x = fOpIntersectionRound(res.x, d, THIS_Smoothradius);
		} else {
			res.x = max(res.x, d);
		}
	}
	return res;
}