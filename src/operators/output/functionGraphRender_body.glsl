vec4 map(vec2 p)
{
	return thismap(p, createDefaultContext());
}

void main()
{
	vec4 color = map(vUV.st);

	#ifdef OUTPUT_COLOR
	colorOut = color;
	#endif
}
