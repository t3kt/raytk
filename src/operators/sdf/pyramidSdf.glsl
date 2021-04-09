ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p.yzx = p.THIS_AXIS_PLANE_SWIZZLE;
	float h = THIS_Height;
	float w = THIS_Width;
	#ifdef THIS_HAS_INPUT_1
	h *= inputOp1(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_2
	w *= inputOp2(p, ctx);
	#endif
	return createSdf(sdPyramid(p / vec3(w, 1., w), h));
}