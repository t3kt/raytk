ReturnT thismap(CoordT p, ContextT ctx) {
	float s = THIS_Scale;
	#ifdef THIS_HAS_INPUT_scaleField
	s *= inputOp_scaleField(p, ctx);
	#endif
	return createSdf(sdTetrahedron((p - THIS_Translate) / s) * s);
}