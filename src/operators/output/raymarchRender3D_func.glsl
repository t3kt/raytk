ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return createNonHitSdf();
	#endif
}

Ray evaluateCamera(vec2 p, CameraContext ctx) {
#ifndef THIS_HAS_INPUT_camera
	mat4 camMat = mat4(
		1., 0., 0., 0.,
		0., 1., 0., 0.,
		0., 0., 1., 0.,
		0., 0., 5., 0.
	);
	return createStandardCameraRay(
		p,
		ctx.resolution,
		0,
		45,
		camMat
	);
#else
	return inputOp_camera(p, ctx);
#endif
}

Ray getViewRay(vec2 shift) {
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution + shift;
	CameraContext ctx;
	ctx.resolution = resolution;
	return evaluateCamera(fragCoord, ctx);
}

#ifdef THIS_USE_LIGHT_FUNC

Light getLight(vec3 p, LightContext ctx) {
	return inputOp3(p, ctx);
}

#endif

#ifdef THIS_HAS_INPUT_secondaryLight
Light getLight2(vec3 p, LightContext ctx) {
	return inputOp_secondaryLight(p, ctx);
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

vec4 getBackgroundColor(in Ray ray) {
	#ifdef THIS_USE_BACKGROUND_FIELD
	RayContext ctx = createRayContext(ray, createNonHitSdf());
	vec4 col = inputOp_backgroundField(ray.pos, ctx);
	#ifndef THIS_Usebackgroundfieldalpha
	col.a = 1.;
	#endif
	return col;
	#else
	return vec4(0.);
	#endif
}

#ifdef RAYTK_USE_SHADOW
float calcShadedLevel(vec3 p, MaterialContext matCtx) {
	#ifdef THIS_HAS_INPUT_shadow
	float res = inputOp_shadow(p, matCtx);
	#else
	float res = calcShadowDefault(p, matCtx);
	#endif
	return res;
}
#endif

vec4 castSecondaryRay(MaterialContext matCtx) {
#ifdef RAYTK_USE_SECONDARY_RAY_CAST
	return inputOp_secondaryRayCast(matCtx.ray.pos, matCtx);
#else
	return vec4(0.);
#endif
}

vec3 getRefractionColor(vec3 p, MaterialContext matCtx) {
	#if defined(RAYTK_USE_REFRACTION) && defined(THIS_HAS_INPUT_refractionRayCast)
	return inputOp_refractionRayCast(matCtx.ray.pos, matCtx).rgb;
	#else
	return vec3(0.);
	#endif
}
