ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_RETURN_TYPE_vec4
	ReturnT res = vec4(inputOp1(p, ctx));
	#else
	ReturnT res = THIS_asReturnT(inputOp1(p, ctx));
	#endif
	res = mapRange(res,
		THIS_asReturnT(THIS_Inputlow), THIS_asReturnT(THIS_Inputhigh),
		THIS_asReturnT(THIS_Outputlow), THIS_asReturnT(THIS_Outputhigh));
	res *= THIS_Multiply * THIS_asReturnT(THIS_Mult);
	return res + THIS_asReturnT(THIS_Postadd);
}