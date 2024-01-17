ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = THIS_Scale;
	#ifdef THIS_HAS_INPUT_scaleField
	size *= fillToVec2(inputOp_scaleField(p, ctx));
	#endif

	#ifdef THIS_HAS_INPUT_chamferField
	vec2 chamfer = fillToVec2(inputOp_chamferField(p, ctx));
	#else
	vec2 chamfer = THIS_Chamfer;
	#endif

	float d = sdChamferRect(p, size, chamfer);

	return createSdf(d);
}