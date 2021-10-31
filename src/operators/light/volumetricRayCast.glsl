ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 res = vec4(0.);
	#pragma r:if THIS_Enablevolumetric
	float totalDist = ctx.result.x;
	bool isMiss = isNonHitSdfDist(totalDist);
	if (THIS_Skipmissedrays > 0. && isMiss) {
		return ReturnT(0.);
	}
	int priorStage = pushStage(RAYTK_STAGE_VOLUMETRIC);
	float level = THIS_Level;
	Ray ray = ctx.ray;
	LightContext lightCtx = createLightContext(ctx.result, ctx.normal);
	#pragma r:if THIS_Recalculatelight
	#pragma r:else
	// For non-hits, this won't be populated by default.
	// and if Recalculatelight isn't used, it won't be updated within the loop below.
	if (isNonHitSdf(ctx.result)) {
		ctx.light = getLight(ray.pos + ray.dir * ctx.result.x, lightCtx);
	}
	#pragma r:endif
	#pragma r:if THIS_Marchmode_fixedstep
	int n = int(THIS_Maxsteps);
	float stepDist = THIS_Fixedstep;
	if (isMiss) {
		totalDist = RAYTK_MAX_DIST;
	}
	#pragma r:elif THIS_Marchmode_divisions
	int n = int(THIS_Stepdivisions);
	if (isMiss) {
		totalDist = THIS_Raymissdist;
	}
	float stepDist = totalDist / float(n);
	#pragma r:else
	#error invalidMarchMode
	#pragma r:endif
	float remainingDist = totalDist;
	for (int i = 0; i < n; i++) {
		float actualStep = min(remainingDist, stepDist);
		if (actualStep <= 0.) break;
		vec3 midPoint = ray.pos + ray.dir * stepDist * 0.5;
		#pragma r:if THIS_Recalculatelight
		ctx.light = getLight(midPoint, lightCtx);
		#pragma r:endif
		#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
		int innerPriorStage = pushStage(RAYTK_STAGE_VOLUMETRIC_SHADOW);
		ctx.shadedLevel = calcShadedLevel(midPoint, ctx);
		popStage(innerPriorStage);
		#pragma r:endif
		float amount = actualStep * level;
		#pragma r:if THIS_HAS_INPUT_lightVolume
		vec4 col = inputOp_lightVolume(midPoint, ctx);
		#pragma r:else
		vec4 col = vec4(1.);
		#pragma r:endif
		res += col * amount;
		ray.pos += ray.dir * actualStep;
		remainingDist -= actualStep;
	}

	popStage(priorStage);
	#pragma r:endif
	return res;
}