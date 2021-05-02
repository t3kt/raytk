ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	inputOp1_ReturnT res1 = inputOp1(p, ctx);
	#if !defined(THIS_HAS_INPUT_2)
	res = res1;
	#elif defined(THIS_RETURN_TYPE_float)
	res = ReturnT(inputOp2(inputOp2_CoordT(res1), ctx));
	#elif defined(THIS_RETURN_TYPE_vec4)
	{
		#ifdef inputOp2_RETURN_TYPE_vec4
		res = inputOp2(res1, ctx);
		#else
		res = ReturnT(
			inputOp2(res1.x, ctx),
			inputOp2(res1.y, ctx),
			inputOp2(res1.z, ctx),
			inputOp2(res1.w, ctx));
		#endif
	}
	#elif defined(THIS_RETURN_TYPE_Sdf)
	res = res1;
	res.x = inputOp2(res1.x, ctx);
	#else
	#error invalidReturnType
	#endif
	return res;
}