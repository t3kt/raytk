out vec4 fragColor;
void main()
{
	vec4 result = vec4(0.);
#if defined(IN_TEX_2D)
	vec2 flatRes = uTDOutputInfo.res.zw;
	vec2 flatUV = vUV.st;
	vec2 inputRes = uTD2DInfos[0].res.zw;
	float index = flatUV.x * flatRes.x + flatUV.y;
	ivec2 inputPx = ivec2(mod(index, inputRes.x), floor(index / inputRes.x));
	vec2 inputUV = vec2(inputPx) / inputRes;
	result = texture(sTD2DInputs[0], inputUV);
#elif defined(IN_TEX_2D_ARRAY)
	vec3 flatRes = vec3(uTDOutputInfo.res.zw, 0.);
#elif defined(IN_TEX_3D)
#else
#endif
	fragColor = TDOutputSwizzle(result);
}
