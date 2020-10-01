#define thismap inputOp1
#ifdef THIS_USE_CAM_FUNC

Ray getViewRay() {
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution;
	CameraContext ctx;
	ctx.resolution = resolution;
	return inputOp2(fragCoord, ctx);
}

#endif

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
