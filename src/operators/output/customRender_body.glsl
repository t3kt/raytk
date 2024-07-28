void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	CustomRenderInputs inputs;
	inputs.uvPos = vec3(vUV.st, 0.);
	inputs.resolution = vec3(uTDOutputInfo.res.zw, 1.);
	#if defined(RAYTK_OUTPUT_TEXTURE_2D)
	#elif defined(RAYTK_OUTPUT_TEXTURE_3D)
	inputs.uvPos.z = uTDOutputInfo.depth.z; // depth offset
	inputs.resolution.z = int(uTDOutputInfo.depth.y); // depth
	#elif defined(RAYTK_OUTPUT_TEXTURE_2D_ARRAY)
	inputs.resolution.z = int(uTDOutputInfo.depth.y);
	if (inputs.resolution.z > 1) {
		inputs.uvPos.z = uTDOutputInfo.depth.z / (inputs.resolution.z - 1.0);
	}
	#endif
	inputs.pixelPos = ivec3(inputs.uvPos * inputs.resolution);

	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	vec2 p = fragCoord*2. - vec2(1.);

	pushStage(RAYTK_STAGE_PRIMARY);

	Context ctx = createDefaultContext();

	customMain(inputs, ctx);
}