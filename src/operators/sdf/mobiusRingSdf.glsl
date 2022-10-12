// https://www.shadertoy.com/view/XsGXR1

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p -= THIS_Translate;
	// standard axis swizzle macros don't match what this needs
	#if defined(THIS_Axis_x)
	p = p.yxz;
	#elif defined(THIS_Axis_y)
	#elif defined(THIS_Axis_z)
	p = p.yzx;
	#else
	#error invalidAxis
	#endif

	#ifdef THIS_EXPOSE_angle
	THIS_angle = degrees(atan(p.x, p.z)) + 180.;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(p.x, p.z)/TAU - .5;
	#endif

	#ifdef THIS_HAS_INPUT_thicknessField
	float thickness = inputOp_thicknessField(p0, ctx);
	#else
	float thickness = THIS_Thickness;
	#endif

	#ifdef THIS_HAS_INPUT_radiusField
	float radius = inputOp_radiusField(p0, ctx);
	#else
	float radius = THIS_Radius;
	#endif

	float rounding = THIS_Rounding;
	float twist = THIS_Twist;
	float twistPhase = THIS_Twistphase;
	vec3 q = vec3(length(p.xz) - radius, 0., p.y);
	float a = atan (p.z, p.x) + twistPhase * PI;
	pR(q.zx, twist * a);
	return createSdf(0.5 * (length(max(abs(q.xz) - thickness, 0.)) - rounding));
}