ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable)) return res;
	#ifdef RAYTK_USE_TRANSPARENCY
	float a = THIS_Alpha;
	res.transparent = vec2(1., a);
	#endif
	return res;
}