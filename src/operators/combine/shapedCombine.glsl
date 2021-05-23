ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res1 = inputOp1(p, ctx);
	ReturnT res2 = inputOp2(p, ctx);
	float r = THIS_Radius;
	float a = adaptAsFloat(res1);
	float b = adaptAsFloat(res2);

	float d = adaptAsFloat(inputOp3(vec2(a, b)/r, ctx)) / r;
	ReturnT res;
	#if defined(THIS_RETURN_TYPE_float)
	{
		res = min(min(a, b, d));
	}
	#elif defined(THIS_RETURN_TYPE_Sdf)
	{
		float h = smoothBlendRatio(res1.x, res2.x, r);
		res1.x = min(d, min(res1.x, res2.x));
		blendInSdf(res1, res2, 1.0 - h);
		res = res1;
	}
	#else
	#error invalidReturnType
	#endif
	return res;
}