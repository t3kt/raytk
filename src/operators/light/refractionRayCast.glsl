ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if !defined(RAYTK_USE_REFRACTION) || !defined(THIS_Enablerefraction)
	res = ReturnT(0.);
	#else
	if (!ctx.result.refract) return res;
	int priorStage = pushStage(RAYTK_STAGE_REFRACT);
	bool hit = false;
	for (int i = 0; i < THIS_Refractionpasses; i++) {
		if (!ctx.result.refract) {
			break;
		}
		// For first iteration, normal will already be populated.
		if (i > 0) {
			ctx.normal = calcNormal(p);
		}
		vec3 pEnter = ctx.ray.pos - ctx.normal * RAYTK_SURF_DIST * 1.1; // arbitrary multiplier
		Ray rayInside = Ray(pEnter, refract(ctx.ray.dir, ctx.normal, 1.0 / ctx.result.ior));
		Sdf resInside = castRayBasic(rayInside, RAYTK_MAX_DIST, -1.);
		if (isNonHitSdfDist(-1. * resInside.x)) {
			break;
		}
		vec3 pExit = pEnter + rayInside.dir * resInside.x;
		vec3 nExit = -calcNormal(pExit);
		ctx.ray.pos = pExit;
		ctx.ray.dir = refract(rayInside.dir, nExit, resInside.ior);
		if (dot(ctx.ray.dir, ctx.ray.dir) == 0.) {
			ctx.ray.dir = reflect(rayInside.dir, nExit);
		}
		p = pExit;
		ctx.normal = nExit;
		ctx.ray.pos += ctx.ray.dir * RAYTK_SURF_DIST * 2.;
		hit = true;
	}
	if (hit) {
		res = getColor(ctx.ray.pos, ctx);
		#ifdef OUTPUT_DEBUG
		debugOut.r = 0.9;
		#endif
	} else {
		#ifdef OUTPUT_DEBUG
		debugOut.r = 0.2;
		#endif
	}
	popStage(priorStage);
	#endif
	return res;
}