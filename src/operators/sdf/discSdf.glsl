ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p - THIS_Translate;
	switch (int(THIS_Axis)) {
		case 0: q = q.yxz; break;
		case 1: q = q.zyx; break;
		case 2: q = q.xzy; break;
	}

	#ifdef THIS_EXPOSE_angle
	THIS_angle = degrees(atan(q.x, q.z)) + 180.;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(q.x, q.z)/TAU - .5;
	#endif

	#ifdef THIS_HAS_INPUT_radiusField
	float r = THIS_Radius * inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif

	#ifdef THIS_EXPOSE_normaxisdist
	THIS_normaxisdist = length(q.xz) / r;
	#endif

	#ifdef THIS_HAS_INPUT_thicknessField
	float t = THIS_Thickness * inputOp_thicknessField(p, ctx);
	#else
	float t = THIS_Thickness;
	#endif
	return createSdf(fDisc(q, r) - t);
}