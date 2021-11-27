ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if !defined(THIS_HAS_REF_var)
	res = THIS_asReturnT(THIS_Defaultval);
	#else
	#if defined(THIS_Datatype_vec4) && defined(THIS_RETURN_TYPE_float)
	res = adaptAsVec4(THIS_var).THIS_Part;
	#else
	res = THIS_asReturnT(THIS_var);
	#endif
	#endif
	return res;
}