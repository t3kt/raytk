ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#if !defined(THIS_HAS_INPUT_2)
	#elif defined(THIS_RETURN_TYPE_float)
	res = inputOp2(res, ctx);
	#elif defined(THIS_RETURN_TYPE_vec4)
	res = ReturnT(
		inputOp2(res.x, ctx),
		inputOp2(res.y, ctx),
		inputOp2(res.z, ctx),
		inputOp2(res.w, ctx));
	#elif defined(THIS_RETURN_TYPE_Sdf)
	res.x = inputOp2(res.x, ctx);
	#else
	#error invalidReturnType
	#endif
	return res;
}