ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		p = THIS_asCoordT(THIS_MASK * adaptAsVec3(p).THIS_SWIZZLE);
	}
	return inputOp1(p, ctx);
}
