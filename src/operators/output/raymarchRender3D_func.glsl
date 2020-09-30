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
