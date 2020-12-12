ReturnT thismap(CoordT p, ContextT ctx) {
	return createSdf(sdPyramid((p - THIS_Translate) / vec3(THIS_Width, 1., THIS_Width), THIS_Height));
}