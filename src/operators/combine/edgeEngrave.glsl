ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_USE_RADIUS_FIELD
		float radius = inputOp3(p, ctx);
	#else
		float radius = THIS_Radius;
	#endif
	ReturnT res1 = THIS_INPUT_1(p, ctx);
	ReturnT res2 = THIS_INPUT_2(p, ctx);
	#ifdef THIS_RETURN_TYPE_float
		return fOpEngrave(res1, res2, radius);
	#else
	res1.x = fOpEngrave(res1.x, res2.x, radius);
	res1.interpolant = clamp(0.5 - 0.5*(res2.x+res1.x)/radius, 0., 1.);
	res1.material2 = res2.material;
	return res1;
	#endif
}