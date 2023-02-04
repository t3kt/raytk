ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#if !defined(RAYTK_USE_REFRACTION) || !defined(THIS_Enablerefraction)
	res = ReturnT(0.);
	#else
	if (!ctx.result.refract) return res;
	int priorStage = pushStage(RAYTK_STAGE_REFRACT);
	bool hit = false;
	int n = int(THIS_Refractionpasses);
	for (int i = 0; i < n; i++) {
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
		resInside.x *= -1.;
		if (isNonHitSdfDist(resInside.x)) {
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
//		setDebugOut(vec4(ctx.ray.dir * 2., 0.));
		ctx.normal = nExit;
//		ctx.ray.pos += ctx.ray.dir * RAYTK_SURF_DIST * 2.;
		hit = true;
	}
	if (hit) {
		res = getColor(ctx.ray.pos, ctx);
//		setDebugOut(vec4(1, 0.9, 0., 1));
		#ifdef OUTPUT_DEBUG
//		debugOut.rgb = ctx.ray.pos;
//		debugOut.r = 0.9;
//		debugOut.g = float(n);
		#endif
		setDebugOut(vec4(ctx.ray.dir, 0.));
	} else {
		setDebugOut(vec4(0.2, 0., 0., 1.));
	}
	popStage(priorStage);
	#endif
	return res;
}