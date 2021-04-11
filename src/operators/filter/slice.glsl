ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#ifdef THIS_Enablemirror
	float q = abs(p.THIS_AXIS);
	#else
	float q = p.THIS_AXIS;
	#endif
	float d = abs(q - THIS_Offset) - THIS_Thickness;
	#if defined(THIS_Operation_intersect)
	#elif defined(THIS_Operation_diff)
	{
		d = -d;
	}
	#else
	#error invalidOperation
	#endif
	#ifdef THIS_Enablesmoothing
	res.x = fOpIntersectionRound(res.x, d, THIS_Smoothradius);
	#else
	res.x = max(res.x, d);
	#endif
	return res;
}