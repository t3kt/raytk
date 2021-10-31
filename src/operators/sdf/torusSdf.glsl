ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;

	// Convert to XZ plane expected by fTorus()
	#pragma r:if THIS_Axis_x
	p = p.yxz;
	#pragma r:elif THIS_Axis_y
	p = p.zyx;
	#pragma r:elif THIS_Axis_z
	p = p.xzy;
	#pragma r:endif

	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	float t = THIS_Thickness;
	#pragma r:if THIS_HAS_INPUT_thicknessField
	t *= inputOp_thicknessField(p, ctx);
	#pragma r:endif

	#pragma r:if THIS_Enablecaps
	ReturnT res = createSdf(sdCappedTorus(
		p, vec2(THIS_Startangle, THIS_Endangle), r, t));
	#pragma r:else
	ReturnT res = createSdf(fTorus(p, t, r));
	#pragma r:endif
	#pragma r:if THIS_Uvmode_torus
	float d0 = length(p.xz) - r;
	assignUV(
		res,
		vec3(
			atan(p.x, p.z)/TAU + 0.5, // around axis
			atan(d0, p.y)/TAU + 0.5, // around core
			length(vec2(d0, p.y)) / t // dist from core
		)
	);
	#pragma r:endif
	return res;
}