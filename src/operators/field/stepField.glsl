ReturnT thismap(CoordT p, ContextT ctx) {
	float q;
	#if defined(THIS_HAS_INPUT_1)
	q = inputOp1(p, ctx);
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

	#ifdef THIS_Enableblend
	float x = smoothstep(0, THIS_Blend, q - THIS_Edge);
	#else
	float x = step(THIS_Edge, q);
	#endif

	#ifdef THIS_Reverse
	x = 1.0 - x;
	#endif

	return mix(THIS_asReturnT(THIS_Value1), THIS_asReturnT(THIS_Value2), x);
}