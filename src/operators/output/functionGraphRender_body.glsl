vec4 map(vec2 p)
{
	return thismap(p, createDefaultContext());
}

void main()
{
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	vec4 color = map(vUV.st);

	#ifdef OUTPUT_COLOR
	colorOut = color;
	#endif
}
