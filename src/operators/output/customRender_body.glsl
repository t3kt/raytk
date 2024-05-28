void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	vec2 p = fragCoord*2. - vec2(1.);

	pushStage(RAYTK_STAGE_PRIMARY);

	Context ctx = createDefaultContext();

	customMain(fragCoord, p, ctx);
}