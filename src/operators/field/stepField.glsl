ReturnT thismap(CoordT p, ContextT ctx) {
	float q;
	#if defined(THIS_HAS_INPUT_coordField)
	q = inputOp_coordField(p, ctx);
	#elif defined(THIS_Axis_dist)
	q = length(p);
	#elif defined(THIS_Axis_x) || defined(THIS_COORD_TYPE_float) || (defined(THIS_Axis_z) && defined(THIS_COORD_TYPE_vec2))
	q = extractOrUseAsX(p);
	#elif defined(THIS_Axis_y)
	q = p.y;
	#elif defined(THIS_Axis_z)
	q = p.z;
	#else
	#error invalidCoordinateSource
	#endif

	#ifdef THIS_HAS_INPUT_edgeField
	float edge = inputOp_edgeField(p, ctx);
	#else
	float edge = THIS_Edge;
	#endif
	#ifdef THIS_Enableblend
	float x = smoothstep(0, THIS_Blend, q - edge);
	#else
	float x = step(edge, q);
	#endif

	#ifdef THIS_Reverse
	x = 1.0 - x;
	#endif

	#ifdef THIS_HAS_INPUT_lowValue
	ReturnT low = THIS_asReturnT(inputOp_lowValue(p, ctx));
	#else
	ReturnT low = THIS_asReturnT(THIS_Value1);
	#endif

	#ifdef THIS_HAS_INPUT_highValue
	ReturnT high = THIS_asReturnT(inputOp_highValue(p, ctx));
	#else
	ReturnT high = THIS_asReturnT(THIS_Value2);
	#endif

	return mix(low, high, x);
}