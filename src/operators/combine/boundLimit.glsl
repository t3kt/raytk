ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	float margin = THIS_Margin;
	Sdf boundRes = inputOp2(p, ctx);
	if (boundRes.x - margin > RAYTK_SURF_DIST) {
		return boundRes;
	}
	return inputOp1(p, ctx);
}