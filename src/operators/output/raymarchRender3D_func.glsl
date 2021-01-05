#ifdef THIS_HAS_INPUT_1

#define thismap inputOp1

#else

Sdf thismap(vec3 p, Context ctx) {
	return createSdf(RAYTK_MAX_DIST);
}

#endif

Ray getViewRay(vec2 shift) {
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution + shift;
	CameraContext ctx;
	ctx.resolution = resolution;
	return inputOp2(fragCoord, ctx);
}

#ifdef THIS_USE_LIGHT_FUNC

Light getLight(vec3 p, LightContext ctx) {
	return inputOp3(p, ctx);
}

#endif

#ifdef THIS_USE_LIMIT_BOX
bool checkLimit(vec3 p) {
	return p.x >= THIS_Limitboxminx &&
		p.x <= THIS_Limitboxmaxx &&
		p.x >= THIS_Limitboxminy &&
		p.x <= THIS_Limitboxmaxy &&
		p.x >= THIS_Limitboxminz &&
		p.x <= THIS_Limitboxmaxz;
}
#else
#define checkLimit(p) (true)
#endif

#ifdef THIS_USE_NEAR_HIT

float checkNearHit(float d) {
	if (d > THIS_Nearhitrange) { return 0; }
	return smoothstep(RAYTK_SURF_DIST, THIS_Nearhitrange, d);
}

#endif

#ifdef THIS_USE_RAYMOD_FUNC
void modifyRay(inout Ray ray) {
	RayContext rCtx;
	rCtx.ray = ray;
	ray = inputOp4(ray.pos, rCtx);
//	ray.dir = normalize(ray.dir);
}
#endif
