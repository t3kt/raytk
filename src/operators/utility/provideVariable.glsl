ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_VAR
	{
		#ifdef THIS_HAS_INPUT_valueField
		#ifdef THIS_Datatype_vec4
		vec4 val = adaptAsVec4(inputOp_valueField(p, ctx));
		#elif defined(THIS_Datatype_float)
		float val = adaptAsFloat(inputOp_valueField(p, ctx));
		#endif
		#else
		#ifdef THIS_Datatype_vec4
		vec4 val = THIS_Value;
		#elif defined(THIS_Datatype_float)
		float val = THIS_Value1;
		#endif
		#endif
		THIS_VAR = val;
		#endif
	}
	return inputOp1(p, ctx);
}