ReturnT thismap(CoordT p, ContextT ctx) {
	int priorStage = pushStage(RAYTK_STAGE_NORMAL);
	#ifdef THIS_Enablenormalsmoothing
	vec2 e = vec2(1.0, -1.0) * (0.5773*0.005 + THIS_Normalsmoothing);
	#else
	const vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	#endif
	vec3 n = normalize(
		e.xyy*inputOp1(p + e.xyy, ctx).x +
		e.yyx*inputOp1(p + e.yyx, ctx).x +
		e.yxy*inputOp1(p + e.yxy, ctx).x +
		e.xxx*inputOp1(p + e.xxx, ctx).x);
	popStage(priorStage);
	return ReturnT(n, 0.);
}