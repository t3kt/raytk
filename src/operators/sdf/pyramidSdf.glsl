ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p.yzx = p.THIS_AXIS_PLANE_SWIZZLE;
	return createSdf(sdPyramid(p / vec3(THIS_Width, 1., THIS_Width), THIS_Height));
}