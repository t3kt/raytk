ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	#if defined(THIS_Limittype_off)
		return val;
	#elif defined(THIS_Limittype_clamp)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = clamp(val.x, THIS_LOW, THIS_HIGH);
		#else
		val = clamp(val, THIS_LOW, THIS_HIGH);
		#endif
	#elif defined(THIS_Limittype_zigzag)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = modZigZag(val.x, THIS_LOW, THIS_HIGH);
		#else
		val = modZigZag(val, THIS_LOW, THIS_HIGH);
		#endif
	#elif defined(THIS_Limittype_loop)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = wrapRange(val.x, THIS_LOW, THIS_HIGH);
		#else
		val = wrapRange(val, THIS_LOW, THIS_HIGH);
		#endif
	#else
		#error invalidLimitType
	#endif
	return val;
}