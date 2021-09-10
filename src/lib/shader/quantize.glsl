// quantize.glsl

float quantizeGain(float x, float k)
{
	float a = 0.5*pow(2.0*((x<0.5)?x:1.0-x), k);
	return (x<0.5)?a:1.0-a;
}
vec2 quantizeGain(vec2 x, vec2 k)
{
	return vec2(quantizeGain(x.x, k.x), quantizeGain(x.y, k.y));
}
vec3 quantizeGain(vec3 x, vec3 k)
{
	return vec3(quantizeGain(x.x, k.x), quantizeGain(x.y, k.y), quantizeGain(x.z, k.z));
}
vec4 quantizeGain(vec4 x, vec4 k)
{
	return vec4(quantizeGain(x.x, k.x), quantizeGain(x.y, k.y), quantizeGain(x.z, k.z), quantizeGain(x.w, k.w));
}

float quantize(float p, float size, float offset, float smoothing) {
	p = (p + offset) / size;
	return ((floor(p) + quantizeGain(fract(p), smoothing)) * size) - offset;
}

vec2 quantize(vec2 p, vec2 size, vec2 offset, vec2 smoothing) {
	p = (p + offset) / size;
	return ((floor(p) + quantizeGain(fract(p), smoothing)) * size) - offset;
}

vec3 quantize(vec3 p, vec3 size, vec3 offset, vec3 smoothing) {
	p = (p + offset) / size;
	return ((floor(p) + quantizeGain(fract(p), smoothing)) * size) - offset;
}

vec4 quantize(vec4 p, vec4 size, vec4 offset, vec4 smoothing) {
	p = (p + offset) / size;
	return ((floor(p) + quantizeGain(fract(p), smoothing)) * size) - offset;
}

float quantizeHard(float p, float size, float offset) {
	return (floor((p + offset) / size) * size) - offset;
}

vec4 quantizeHard(vec4 p, vec4 size, vec4 offset) {
	return (floor(p = (p + offset) / size) * size) - offset;
}
