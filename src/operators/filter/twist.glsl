ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		switch (int(THIS_Axis)) {
			case 0: pR(p.yz, p.x * THIS_Amount + THIS_Shift); break;
			case 1: pR(p.zx, p.y * THIS_Amount + THIS_Shift); break;
			case 2: pR(p.xy, p.z * THIS_Amount + THIS_Shift); break;
		}
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}