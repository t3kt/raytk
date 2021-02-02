ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_1)
	return inputOp1(p, ctx);
	#elif defined(THIS_RETURN_TYPE_Sdf)
	return createNonHitSdf();
	#else
	return ReturnT(0.);
	#endif
}
