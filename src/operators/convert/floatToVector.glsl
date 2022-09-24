ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifdef THIS_USE_SINGLE_SOURCE
	{
		#ifdef THIS_INPUT_OP
			res = vec4(THIS_INPUT_OP(p, ctx));
		#else
			res = vec4(THIS_SOURCE);
		#endif
	}
	#else
	{
		#ifdef THIS_USE_INPUT_1
		float input1 = inputOp1(p, ctx);
		#endif
		#ifdef THIS_USE_INPUT_2
		float input2 = inputOp2(p, ctx);
		#endif
		#ifdef THIS_USE_INPUT_3
		float input3 = inputOp3(p, ctx);
		#endif
		#ifdef THIS_USE_INPUT_4
		float input4 = inputOp4(p, ctx);
		#endif
		res = vec4(
			THIS_SOURCE_X,
			THIS_SOURCE_Y,
			THIS_SOURCE_Z,
			THIS_SOURCE_W
		);
	}
	#endif
	return res;
}