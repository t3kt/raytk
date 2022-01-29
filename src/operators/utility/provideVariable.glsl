ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_VAR
	{
		#ifdef THIS_HAS_INPUT_valueField
			THIS_VAR = THIS_VAR_asVarT(inputOp_valueField(p, ctx));
		#else
			THIS_VAR = THIS_VAR_asVarT(THIS_Value);
		#endif
	}
	#endif
	return inputOp1(p, ctx);
}