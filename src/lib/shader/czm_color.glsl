// https://github.com/CesiumGS/cesium/blob/master/Source/Shaders/Builtin/Functions/
vec3 czm_saturation(vec3 rgb, float adjustment)
{
	// Algorithm from Chapter 16 of OpenGL Shading Language
	const vec3 W = vec3(0.2125, 0.7154, 0.0721);
	vec3 intensity = vec3(dot(rgb, W));
	return mix(intensity, rgb, adjustment);
}
// adjustment is in radians
vec3 czm_hue(vec3 rgb, float adjustment)
{
	const mat3 toYIQ = mat3(0.299,     0.587,     0.114,
	0.595716, -0.274453, -0.321263,
	0.211456, -0.522591,  0.311135);
	const mat3 toRGB = mat3(1.0,  0.9563,  0.6210,
	1.0, -0.2721, -0.6474,
	1.0, -1.107,   1.7046);

	vec3 yiq = toYIQ * rgb;
	float hue = atan(yiq.z, yiq.y) + adjustment;
	float chroma = sqrt(yiq.z * yiq.z + yiq.y * yiq.y);

	vec3 color = vec3(yiq.x, chroma * cos(hue), chroma * sin(hue));
	return toRGB * color;
}
