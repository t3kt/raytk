ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = ReturnT(0.);
	#ifdef THIS_UseInput1
	inputOp1_ReturnT val1 = inputOp1(p, ctx);
	#endif
	#ifdef THIS_UseInput2
	inputOp2_ReturnT val2 = inputOp2(p, ctx);
	#endif
	#ifdef THIS_UseInput3
	inputOp3_ReturnT val3 = inputOp3(p, ctx);
	#endif
	#ifdef THIS_UseInput4
	inputOp4_ReturnT val4 = inputOp4(p, ctx);
	#endif
	#if defined(THIS_RETURN_TYPE_float)
	{
		val = THIS_Expr1;
	}
	#elif defined(THIS_RETURN_TYPE_vec4)
	{
		val = vec4(
		extractOrUseAsX(THIS_ExprX),
		extractOrUseAsY(THIS_ExprY),
		extractOrUseAsZ(THIS_ExprZ),
		extractOrUseAsW(THIS_ExprW)
		);
	}
	#else
	#error invalidReturnType
	#endif
	return val;
}