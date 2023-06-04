ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.zxy; break;
		case 1: p = p.xyz; break;
		case 2: p = p.yzx; break;
	}
	float pd = -p.y;
	float h = THIS_Height;
	float w = THIS_Width;
	#ifdef THIS_HAS_INPUT_heightField
	h *= inputOp_heightField(p0, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_widthField
	w *= inputOp_widthField(p0, ctx);
	#endif
	float d = sdPyramid(p, h, w);
	return createSdf(d);
}