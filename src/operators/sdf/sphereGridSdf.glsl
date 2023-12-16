ReturnT thismap(CoordT p, ContextT ctx) {
	float rows = float(THIS_Rows);
	float cols = float(THIS_Cols);

	#ifdef THIS_HAS_INPUT_radiusField
	float radius = inputOp_radiusField(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif

	float d;
	BODY();

	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif

	d -= th;
	return createSdf(d);
}