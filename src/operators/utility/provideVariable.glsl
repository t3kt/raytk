ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifdef THIS_Valuesource_primary
	{
		res = inputOp1(p, ctx);
		#ifdef THIS_EXPOSE_VAR
		{
			THIS_VAR = THIS_VAR_asVarT(res);
		}
		#endif
	}
	#else
	{
		#ifdef THIS_EXPOSE_VAR
		{
				#ifdef THIS_HAS_INPUT_valueField
					THIS_VAR = THIS_VAR_asVarT(inputOp_valueField(p, ctx));
				#else
					THIS_VAR = THIS_VAR_asVarT(THIS_Value);
				#endif
		}
		#endif
		res = inputOp1(p, ctx);
	}
	#endif
	return res;
}