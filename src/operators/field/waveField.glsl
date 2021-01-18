ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_2
	float period = THIS_Period * inputOp2(p, ctx);
	#else
	float period = THIS_Period;
	#endif
	#if defined(THIS_HAS_INPUT_1)
		#ifdef THIS_RETURN_TYPE_Sdf
		Sdf res = inputOp1(p, ctx);
		float val = THIS_FUNC((res.x / period) + THIS_Phase);
		res.x = (val * THIS_Amplitude) + THIS_Offset;
		return res;
		#else
		ReturnT q = inputOp1(p, ctx);
		#endif
	#elif defined(THIS_COORD_TYPE_float)
		float q = p;
	#else
		float q = p.THIS_Axis;
	#endif
	ReturnT val = THIS_FUNC((q / period) + THIS_Phase);
	return (val * THIS_Amplitude) + THIS_Offset;
}