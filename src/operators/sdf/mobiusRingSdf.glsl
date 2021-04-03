ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float t = THIS_Thickness;
	// standard axis swizzle macros don't match what this needs
	#if defined(THIS_Axis_x)
	p = p.yxz;
	#elif defined(THIS_Axis_y)
	p = p.yzx;
	#elif defined(THIS_Axis_z)
	#else
	#error invalidAxis
	#endif
	#ifdef THIS_HAS_INPUT_1
	#if defined(inputOp1_COORD_TYPE_float)
	t *= inputOp1(atan(p.z, p.x), ctx);
	#elif defined(inputOp1_COORD_TYPE_vec3)
	t *= inputOp1(p, ctx);
	#else
	#error invalidRadiusCoordType
	#endif
	#endif
	return createSdf(sdMobiusRing(p, THIS_Radius, t, THIS_Rounding, THIS_Twist, THIS_Twistphase));
}