out vec4 fragColor;
void main()
{
	TDCheckDiscard();
	vec4 color = vec4(1.0);
	TDAlphaTest(color.a);
	fragColor = TDOutputSwizzle(color);
}
