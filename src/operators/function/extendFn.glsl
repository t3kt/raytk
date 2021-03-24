ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Extend_hold)
	p = clamp(p, THIS_Range1, THIS_Range2);
	#elif defined(THIS_Extend_cycle)
	p = wrapRange(p, CoordT(THIS_Range1), CoordT(THIS_Range2));
	#elif defined(THIS_Extend_mirror)
	p = modZigZag(p, CoordT(THIS_Range1), CoordT(THIS_Range2));
	#elif defined(THIS_Extend_default)
	if (!allInRange(p, CoordT(THIS_Range1), CoordT(THIS_Range2))) {
		#ifdef THIS_RETURN_TYPE_Sdf
		return createSdf(THIS_Defval);
		#else
		return ReturnT(THIS_Defval);
		#endif
	}
	#else
	#error invalidExtendMode
	#endif
	return inputOp1(p, ctx);
}