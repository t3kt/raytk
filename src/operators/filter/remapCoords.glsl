ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p2 = THIS_asCoordT(inputOp_coordField(p, ctx));
	#if defined(THIS_Remapmode_replace)
	CoordT q = p2;
	#elif defined(THIS_Remapmode_add)
	CoordT q = p + p2;
	#elif defined(THIS_Remapmode_multiply)
	CoordT q = p * p2;
	#else
	#error invalidRemapMode
	#endif
	q = mix(p, q, THIS_Mix);
	return inputOp1(q, ctx);
}