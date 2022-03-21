ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_RETURN_TYPE_vec4) && defined(inputOp1_RETURN_TYPE_float)
	ReturnT res = fillToVec4(inputOp1(p, ctx));
	#else
	ReturnT res = THIS_asReturnT(inputOp1(p, ctx));
	#endif
	if (THIS_Enable >= 0.5) {
		res = mapRange(res,
			THIS_asReturnT(THIS_Inputlow), THIS_asReturnT(THIS_Inputhigh),
			THIS_asReturnT(THIS_Outputlow), THIS_asReturnT(THIS_Outputhigh));
		res *= THIS_Multiply * THIS_asReturnT(THIS_Mult);
		res += THIS_asReturnT(THIS_Postadd);
	}
	return res;
}