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
