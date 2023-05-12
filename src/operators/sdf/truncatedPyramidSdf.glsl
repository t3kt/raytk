ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.zxy; break;
		case 1: p = p.xyz; break;
		case 2: p = p.yzx; break;
	}
	vec2 bottomSize = THIS_Bottomsize;
	vec2 topSize = THIS_Topsize;
	float h = THIS_Height;
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = saturate(p.y / h);
	#endif
	#ifdef THIS_HAS_INPUT_heightField
	h *= inputOp_heightField(p0, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_bottomSizeField
	bottomSize *= fillToVec2(inputOp_bottomSizeField(p0, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_topSizeField
	topSize *= fillToVec2(inputOp_topSizeField(p0, ctx));
	#endif
	float d = sdTruncatedPyramid(p, bottomSize, topSize, h);
	return createSdf(d);
}