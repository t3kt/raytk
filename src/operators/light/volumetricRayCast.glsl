ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 res = vec4(0.);
	#ifdef THIS_Enablevolumetric
	float totalDist = ctx.result.x;
	bool isMiss = isNonHitSdfDist(totalDist);
	if (IS_TRUE(THIS_Skipmissedrays) && isMiss) {
		return ReturnT(0.);
	}
	int priorStage = pushStage(RAYTK_STAGE_VOLUMETRIC);
	float level = THIS_Level;
	Ray ray = ctx.ray;
	LightContext lightCtx = createLightContext(ctx.result, ctx.normal);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	lightCtx.globalPos = ctx.globalPos;
	#endif
	#if !defined(THIS_Recalculatelight)
	// For non-hits, this won't be populated by default.
	// and if Recalculatelight isn't used, it won't be updated within the loop below.
	if (isNonHitSdf(ctx.result)) {
		ctx.light = getLight(ray.pos + ray.dir * ctx.result.x, lightCtx);
	}
	#endif
	#if defined(THIS_Marchmode_fixedstep)
	int n = int(THIS_Maxsteps);
	float stepDist = THIS_Fixedstep;
	if (isMiss) {
		totalDist = RAYTK_MAX_DIST;
	}
	#elif defined(THIS_Marchmode_divisions)
	int n = int(THIS_Stepdivisions);
	if (isMiss) {
		totalDist = THIS_Raymissdist;
	}
	float stepDist = totalDist / float(n);
	#else
	#error invalidMarchMode
	#endif
	float remainingDist = totalDist;
	for (int i = 0; i < n; i++) {
		float actualStep = min(remainingDist, stepDist);
		if (actualStep <= 0.) break;
		vec3 midPoint = ray.pos + ray.dir * stepDist * 0.5;
		#ifdef THIS_Recalculatelight
		ctx.light = getLight(midPoint, lightCtx);
		#endif
		#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
		int innerPriorStage = pushStage(RAYTK_STAGE_VOLUMETRIC_SHADOW);
		ctx.shadedLevel = calcShadedLevel(midPoint, ctx);
		popStage(innerPriorStage);
		#endif
		float amount = actualStep * level;
		#ifdef THIS_HAS_INPUT_lightVolume
		vec4 col = inputOp_lightVolume(midPoint, ctx);
		#else
		vec4 col = vec4(1.);
		#endif
		res += col * amount;
		ray.pos += ray.dir * actualStep;
		remainingDist -= actualStep;
	}

	popStage(priorStage);
	#endif
	return res;
}