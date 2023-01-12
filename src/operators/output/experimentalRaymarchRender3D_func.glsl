ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifdef THIS_HAS_INPUT_sdf
	res = inputOp_sdf(p, ctx);
	#else
	res = createNonHitSdf();
	#endif
	return res;
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

Light getLight(vec3 p, LightContext ctx) {
	Light light;
	#ifdef THIS_HAS_INPUT_light
	light = inputOp_light(p, ctx);
	#else
	light = createLight(vec3(0.), vec3(5.8, 4., 3.5));
	#endif
	return light;
}

bool checkLimit(vec3 p) {
	bool res = true;
	#ifdef THIS_Uselimitbox
	res = p.x >= THIS_Limitboxmin.x &&
		p.x <= THIS_Limitboxmax.x &&
		p.x >= THIS_Limitboxmin.y &&
		p.x <= THIS_Limitboxmax.y &&
		p.x >= THIS_Limitboxmin.z &&
		p.x <= THIS_Limitboxmax.z;
	#endif
	return res;
}
