ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Scaletype_uniform)
	float scale = THIS_Uniformscale;
	#ifdef THIS_HAS_INPUT_2
	scale *= adaptAsFloat(inputOp2(p, ctx));
	#endif
	float adjust = scale;
	#elif defined(THIS_Scaletype_separate)
	CoordT scale = THIS_asCoordT(THIS_Scale);
	#ifdef THIS_HAS_INPUT_2
	scale *= THIS_asCoordT(fillToVec3(inputOp2(p, ctx)));
	#endif
	float adjust = vmin(scale);
	#else
	#error invalidScaleType
	#endif

	ReturnT res = inputOp1(p / scale, ctx);
	#ifdef THIS_RETURN_TYPE_float
	res *= adjust;
	#else
	res.x *= adjust;
	#endif
	return res;
}
