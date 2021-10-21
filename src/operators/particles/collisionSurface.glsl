vec3 THIS_calcNormal(CoordT p, ContextT ctx) {
	const vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	int priorStage = pushStage(RAYTK_STAGE_NORMAL);
	vec3 n = normalize(
		e.xyy*inputOp_surface(p + e.xyy, ctx).x +
		e.yyx*inputOp_surface(p + e.yyx, ctx).x +
		e.yxy*inputOp_surface(p + e.yxy, ctx).x +
		e.xxx*inputOp_surface(p + e.xxx, ctx).x);
	popStage(priorStage);
	return n;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = ctx.particle;
	if (THIS_Active < 0.5) { return part; }
	BODY();
	return part;
}