ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_VAR
	#ifdef THIS_Datatype_vec4
	THIS_VAR = THIS_Value;
	#elif defined(THIS_Datatype_float)
	THIS_VAR = THIS_Value1;
	#endif
	#endif
	return inputOp1(p, ctx);
}