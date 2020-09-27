ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	#if defined(THIS_LIMIT_clamp)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = clamp(val.x, THIS_LOW, THIS_HIGH);
		return val;
		#else
		return clamp(val, THIS_LOW, THIS_HIGH);
		#endif
	#elif defined(THIS_LIMIT_zigzag)
		#ifdef THIS_RETURN_TYPE_Sdf
		val.x = modZigZag(val.x, THIS_LOW, THIS_HIGH);
		return val;
		#else
		return modZigZag(val, THIS_LOW, THIS_HIGH);
		#endif
	#else
		return val;
	#endif
}