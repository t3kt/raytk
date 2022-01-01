// https://www.shadertoy.com/view/XsGXR1
//float sdMobiusRingStepped(vec3 p, float radius, float thickness, float rounding, float twist, float steps)
//{
//	float d, a, na, aq;
//	vec3 q = vec3(length(p.xz) - radius, 0., p.y);
//	a = atan (p.z, p.x);
//	pR(q.zx, twist * a);
//	d = length(max(abs(q.xz) - thickness, 0.)) - rounding;
//	q = p;
//	na = floor(steps * atan(q.z, - q.x) / (2. * PI));
//	aq = 2. * PI * (na + 0.5) / steps;
//	pR(q.zx, aq);
//	q.x += radius;
//	pR(q.yx, 0.5 * aq);
//	d = max(
//		d,
//		- max(
//				fBox(q, vec3 (1.1, 1.1, 0.18) * thickness)
//				,
//				-fBox2(q.xy, vec2 (0.5, 0.5) * thickness)
//		)
//	);
//	return 0.5 * d;
//}

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float thickness = THIS_Thickness;
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
	#if defined(inputOp_thicknessField_COORD_TYPE_float)
	thickness *= inputOp_thicknessField(atan(p.z, p.x), ctx);
	#elif defined(inputOp_thicknessField_COORD_TYPE_vec3)
	thickness *= inputOp_thicknessField(p, ctx);
	#else
	#error invalidRadiusCoordType
	#endif
	#endif
	float radius = THIS_Radius;
	float rounding = THIS_Rounding;
	float twist = THIS_Twist;
	float twistPhase = THIS_Twistphase;
	vec3 q = vec3(length(p.xz) - radius, 0., p.y);
	float a = atan (p.z, p.x) + twistPhase * PI;
	pR(q.zx, twist * a);
	return createSdf(0.5 * (length(max(abs(q.xz) - thickness, 0.)) - rounding));
}