ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = ReturnT(0.);
	#pragma r:if THIS_UseInput1
	inputOp1_ReturnT val1 = inputOp1(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_UseInput2
	inputOp2_ReturnT val2 = inputOp2(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_UseInput3
	inputOp3_ReturnT val3 = inputOp3(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_UseInput4
	inputOp4_ReturnT val4 = inputOp4(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_RETURN_TYPE_float
	{
		val = THIS_Expr1;
	}
	#pragma r:elif THIS_RETURN_TYPE_vec4
	{
		val = vec4(
		extractOrUseAsX(THIS_ExprX),
		extractOrUseAsY(THIS_ExprY),
		extractOrUseAsZ(THIS_ExprZ),
		extractOrUseAsW(THIS_ExprW)
		);
	}
	#pragma r:else
	#error invalidReturnType
	#pragma r:endif
	return val;
}