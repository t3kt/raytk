ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_1)
	if (IS_TRUE(THIS_Enable)) {
		return THIS_asReturnT(inputOp1(p, ctx));
	}
	#endif
	ReturnT res;
	initDefVal(res);
	#if defined(THIS_HAS_INPUT_2)
	res = THIS_asReturnT(inputOp2(p, ctx));
	#elif defined(THIS_RETURN_TYPE_float) || defined(THIS_RETURN_TYPE_vec4)
	res = THIS_asReturnT(THIS_Defaultvalue);
	#else
	#endif
	return res;
}