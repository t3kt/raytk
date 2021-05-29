// @Param1 {"default":1, "normMin":0, "normMax":2}

ReturnT thismap(CoordT p, Context ctx) {
	#if defined(THIS_RETURN_TYPE_Sdf)
	return createNonHitSdf();
	#elif defined(THIS_RETURN_TYPE_float) || defined(THIS_RETURN_TYPE_vec4)
	return ReturnT(0.);
	#else
	#endif
}