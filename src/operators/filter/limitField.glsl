ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	ReturnT low = THIS_asReturnT(THIS_Low);
	ReturnT high = THIS_asReturnT(THIS_High);
	#if defined(THIS_Limittype_off)
		return val;
	#elif defined(THIS_Limittype_clamp)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = clamp(val.x, low, high);
		#else
		val = clamp(val, low, high);
		#endif
	#elif defined(THIS_Limittype_zigzag)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = modZigZag(val.x, low, high);
		#else
		val = modZigZag(val, low, high);
		#endif
	#elif defined(THIS_Limittype_loop)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = wrapRange(val.x, low, high);
		#else
		val = wrapRange(val, low, high);
		#endif
	#else
		#error invalidLimitType
	#endif
	return val;
}