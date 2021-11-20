ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_REF_var
	return THIS_asReturnT(THIS_var);
	#else
	return THIS_asReturnT(THIS_Defaultval);
	#endif
}