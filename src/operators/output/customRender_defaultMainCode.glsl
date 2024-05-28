void customMain(vec2 fragCoord, vec2 p, Context ctx) {
    vec4 res1 = fillToVec4(thismap(p, ctx));
	#ifdef OUTPUT_COLOR
    colorOut = TDOutputSwizzle(res1);
    #endif
}
