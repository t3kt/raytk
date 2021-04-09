void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	vec2 p = fragCoord*2. - vec2(1.);

	#if defined(THIS_RETURN_TYPE_float)
	vec4 color = vec4(thismap(p, createDefaultContext()));
	#elif defined(THIS_RETURN_TYPE_vec4)
	vec4 color = thismap(p, createDefaultContext);
	#else
	vec4 color = vec4(0.);
	#endif
	
	#ifdef OUTPUT_COLOR
	colorOut = TDOutputSwizzle(color);
	#endif
}