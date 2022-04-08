ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#ifdef THIS_HAS_INPUT_heightField
	float height = THIS_Height * inputOp_heightField(p, ctx);
	#else
	float height = THIS_Height;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float radiusMod = inputOp_radiusField(p, ctx);
	#else
	const float radiusMod = 1.;
	#endif
	switch (int(THIS_Axis)) {
		case 0: p = p.yxz; break;
		case 1: p = p.zyx; break;
		case 2: p = p.xzy; break;
	}
	ReturnT res;
	BODY();
	return res;
}