void customMain(CustomRenderInputs inputs, Context ctx) {
	vec2 p = inputs.uvPos.xy * vec2(2.) - vec2(1.);
	vec4 res1 = fillToVec4(inputOp1(p, ctx));
	#ifdef OUTPUT_COLOR
	colorOut = TDOutputSwizzle(res1);
	#endif
}
