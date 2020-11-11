Sdf thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_USE_RADIUS_FIELD
	float radius = inputOp3(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	Sdf res1 = THIS_INPUT_1(p, ctx);
	Sdf res2 = THIS_INPUT_2(p, ctx);
	res1.x = THIS_FUNC(res1.x, res2.x, radius, THIS_Number);
	float h = clamp(0.5 + 0.5*(res2.x-res1.x)/radius, 0.0, 1.0);
	blendInSdf(res1, res2, h);
	return res1;
}