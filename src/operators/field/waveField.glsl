ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_USE_INPUT)
		#ifdef THIS_RETURN_TYPE_Sdf
		Sdf res = inputOp1(p, ctx);
		float val = THIS_FUNC((res.x / THIS_Period) + THIS_Phase);
		res.x = (val * THIS_Amplitude) + THIS_Offset;
		return res;
		#else
		ReturnT q = inputOp1(p, ctx);
		#endif
	#elif defined(THIS_COORD_TYPE_float)
		float q = p;
	#else
		float q = p.THIS_AXIS;
	#endif
	ReturnT val = THIS_FUNC((q / THIS_Period) + THIS_Phase);
	return (val * THIS_Amplitude) + THIS_Offset;
}