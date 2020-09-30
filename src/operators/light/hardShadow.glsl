float thismap(vec3 p, MaterialContext ctx) {
	vec3 lightVec = normalize(ctx.light.pos - p);
	Ray shadowRay = Ray(p+ctx.normal * SURF_DIST*2., lightVec);
	float shadowDist = castRay(shadowRay, MAX_DIST).x;
	float dist = length(ctx.light.pos - p);
	if (shadowDist < dist) {
		return THIS_Shadowlevel;
	}
	return 1.0;
}
