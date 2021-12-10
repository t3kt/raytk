ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_pos
	THIS_pos = adaptAsVec3(p);
	#endif
	return inputOp1(p, ctx);
}