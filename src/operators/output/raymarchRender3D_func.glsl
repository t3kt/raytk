Sdf thismap(vec3 p, Context ctx) {
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return createNonHitSdf();
	#endif
}

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
	float fade = THIS_Nearhitfade;
	float maxD = THIS_Nearhitrange;
	#ifdef THIS_Enablenearhitmindist
	float minD = THIS_Nearhitmindist;
	if (d < minD || d > maxD) { return 0.; }
	if (d < minD + fade) { return smoothstep(0., fade, d - minD); }
	return 1. - smoothstep(maxD - fade, maxD, d);
	#else
	return 1. - smoothstep(0., fade, d - maxD);
	#endif
}

#endif

#ifdef THIS_USE_RAYMOD_FUNC
void modifyRay(inout Ray ray, in Sdf res) {
	RayContext rCtx = createRayContext(ray, res);
	ray = inputOp4(ray.pos, rCtx);
}
#endif
