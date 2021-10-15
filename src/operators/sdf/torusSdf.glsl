ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;

	// Convert to XZ plane expected by fTorus()
	#if defined(THIS_Axis_x)
	p = p.yxz;
	#elif defined(THIS_Axis_y)
	p = p.zyx;
	#elif defined(THIS_Axis_z)
	p = p.xzy;
	#endif

	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	float t = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_thicknessField
	t *= inputOp_thicknessField(p, ctx);
	#endif

	#ifdef THIS_Enablecaps
	ReturnT res = createSdf(sdCappedTorus(
		p, vec2(THIS_Startangle, THIS_Endangle), r, t));
	#else
	ReturnT res = createSdf(fTorus(p, t, r));
	#endif
	#ifdef THIS_Uvmode_torus
	float d0 = length(p.xz) - r;
	assignUV(
		res,
		vec3(
			atan(p.x, p.z)/TAU + 0.5, // around axis
			atan(d0, p.y)/TAU + 0.5, // around core
			length(vec2(d0, p.y)) / t // dist from core
		)
	);
	#endif
	return res;
}