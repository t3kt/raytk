void THIS_step(
	inout Ray ray,
	inout ContextT ctx,
	inout LightContext lightCtx,
	inout vec4 accum,
	float stepDist,
	float amount) {
	vec3 midPoint = ray.pos + ray.dir * stepDist * 0.5;
	#ifdef THIS_Recalculatelight
	ctx.light = getLight(midPoint, lightCtx);
	#endif
	accum += inputOp1(midPoint, ctx) * amount;
	ray.pos += ray.dir + stepDist;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 res = vec4(0.);
	#ifdef THIS_Enablevolumetric
	if (THIS_Skipmissedrays > 0. && isNonHitSdf(ctx.result)) {
		return ReturnT(0.);
	}
	int priorStage = pushStage(RAYTK_STAGE_VOLUMETRIC);
	Ray ray = ctx.ray;
	LightContext lightCtx = createLightContext(ctx.result, ctx.normal);
	float remainingDist = ctx.result.x;
	#if defined(THIS_Marchmode_fixedstep)
	int n = int(THIS_Maxsteps);
	float stepDist = THIS_Fixedstep;
	#elif defined(THIS_Marchmode_divisions)
	int n = int(THIS_Stepdivisions);
	if (isNonHitSdf(ctx.result)) {
		remainingDist = THIS_Raymissdist;
	}
	float stepDist = remainingDist / float(n);
	#else
	#error invalidMarchMode
	#endif
	for (int i = 0; i < n; i++) {
		#ifdef THIS_Marchmode_fixedstep
		float actualStep = min(remainingDist, stepDist);
		if (actualStep <= 0.) break;
		#else
		float actualStep = stepDist;
		#endif
		THIS_step(
		ray, ctx, lightCtx,
		res,
		actualStep,
		actualStep
		);
		#ifdef THIS_Marchmode_fixedstep
		remainingDist -= actualStep;
		#endif
	}

	popStage(priorStage);
	#endif
	return accum;
}