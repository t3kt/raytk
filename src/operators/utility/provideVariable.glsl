ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_var
	#ifdef THIS_Datatype_vec4
	THIS_var = THIS_Value;
	#elif THIS_Datatype_float
	THIS_var = THIS_Value1;
	#endif
	#endif
	return inputOp1(p, ctx);
}