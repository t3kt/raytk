Sdf thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_3
	float radius = THIS_Radius * inputOp3(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_4
	float offset = THIS_Offset + inputOp4(p, ctx);
	#else
	float offset = THIS_Offset;
	#endif
	Sdf res1 = THIS_INPUT_1(p, ctx);
	Sdf res2 = THIS_INPUT_2(p, ctx);
	res1.x = THIS_FUNC(res1.x, res2.x, radius, THIS_Number, offset * radius);
	float h = clamp(0.5 - 0.5*(res2.x+res1.x)/radius, 0., 1.);
	blendInSdf(res1, res2, h);
	return res1;
}