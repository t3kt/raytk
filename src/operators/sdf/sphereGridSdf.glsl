ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	float rows = float(THIS_Rows);
	float cols = float(THIS_Cols);

	switch (int(THIS_Axis)) {
		case 0: p = p.yzx; break;
		case 1: p = p.zxy; break;
		case 2: p = p.xyz; break;
	}

	#ifdef THIS_HAS_INPUT_radiusField
	float radius = inputOp_radiusField(p0, ctx);
	#else
	float radius = THIS_Radius;
	#endif

	float d;
	BODY();

	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p0, ctx);
	#else
	float th = THIS_Thickness;
	#endif

	d -= th;
	return createSdf(d);
}