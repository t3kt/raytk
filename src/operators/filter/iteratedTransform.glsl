ReturnT thismap(CoordT p, ContextT ctx) {
	float valueAdjust = 1.0;
	int n = int(THIS_Iterations);
	for (int i = 0; i < n; i++) {
		THIS_REFLECT();
		TRANSFORM_CODE();
	}
	ReturnT res = inputOp1(p, ctx);
#ifdef THIS_RETURN_TYPE_Sdf
	res.x *= valueAdjust;
	return res;
#else
	return res * valueAdjust;
#endif
}