Sdf thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HEIGHT_FIELD
	float height = THIS_Height * inputOp1(p, ctx);
	#else
	float height = THIS_Height;
	#endif
	#ifdef THIS_RADIUS_FIELD
	float radiusMod = inputOp2(p, ctx);
	#else
	const float radiusMod = 1.;
	#endif
	return createSdf(THIS_EXPR);
}