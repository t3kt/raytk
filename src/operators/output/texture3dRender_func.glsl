#ifdef THIS_RETURN_TYPE_Sdf

Light getLight(vec3 p, LightContext ctx) {
	Light res;
	#ifdef THIS_HAS_INPUT_light
	res = inputOp_light(p, ctx);
	#else
	res = createLight(vec3(0.), vec3(5.8, 4., 3.5));
	#endif
	return res;
}

Ray getViewRay(vec3 p) {
	vec2 resolution = vec2(256., 256.); // dummy resolution
	vec2 uv = resolution / 2.; // dummy uv
	CameraContext ctx = createCameraContext(resolution);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = p;
	#endif
	Ray ray;
	#ifdef THIS_HAS_INPUT_camera
	ray = inputOp_camera(uv, ctx);
	#else
	ray.pos = vec3(0., 0., 5.);
	#endif
	// Ignore the direction from the camera, and just use the direction from the camera to the point
	ray.dir = normalize(p - ray.pos);
	return ray;
}

float getLevel(Sdf res) {
	float level = 1.0;
	float b = 0.;
	float t = THIS_Thickness / 2.;
	if (IS_TRUE(THIS_Enableblending)) {
		b = THIS_Blending;
	}
	float d = res.x;
	MATERIAL_MODE_BODY();
	return level;
}

#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	initDefVal(res);
	#ifdef THIS_HAS_INPUT_primary
	res = inputOp_primary(p, ctx);
	#endif
	return res;
}