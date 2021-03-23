float thismap(vec3 p, MaterialContext ctx) {
	vec3 lightVec = normalize(ctx.light.pos - p);
	Ray shadowRay = Ray(p+ctx.normal * RAYTK_SURF_DIST*2., lightVec);
	int priorStage = pushStage(RAYTK_STAGE_SHADOW);
	float shadowDist = castRayBasic(shadowRay, RAYTK_MAX_DIST).x;
	popStage(priorStage);
	float dist = length(ctx.light.pos - p);
	if (shadowDist < dist) {
		return THIS_Shadowlevel;
	}
	return 1.0;
}
