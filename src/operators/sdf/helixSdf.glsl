ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	float thickness = THIS_Thickness;
	float radius = THIS_Radius;
	#ifdef THIS_HAS_INPUT_1
	#if defined(inputOp1_COORD_TYPE_float)
	thickness *= inputOp1(p.y, ctx);
	#elif defined(inputOp1_COORD_TYPE_vec2)
	thickness *= inputOp1(vec2(p.y, degrees(atan(p.z, p.x))), ctx);
	#elif defined(inputOp1_COORD_TYPE_vec3)
	thickness *= inputOp1(p, ctx);
	#endif
	#endif
	#ifdef THIS_HAS_INPUT_2
	#if defined(inputOp2_COORD_TYPE_float)
	radius *= inputOp2(p.y, ctx);
	#elif defined(inputOp2_COORD_TYPE_vec3)
	radius *= inputOp2(p, ctx);
	#endif
	#endif
	return createSdf(sdHelix(
		p, radius, thickness, THIS_Spread, THIS_Dualspread * radius));
}