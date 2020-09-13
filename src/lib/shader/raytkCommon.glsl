// raytkCommon.glsl

struct Sdf
{
	float x; // distance
	float material; // material ID
	float material2; // in case of interpolating, the second material
	float interpolant; // in case of interpolating, the interpolation value
	float ior; // index of refraction in case of refraction
	bool reflect; // do reflection for this?
	bool refract; // do refraction for this?
};

Sdf createSdf(float dist) {
	Sdf res;
	res.x = dist;
	res.material = 2;
	res.reflect = false;
	res.refract = false;
	res.material2 = 0.;
	res.interpolant = 0.;
	return res;
}

struct Context {
	vec4 iteration;
};

Context createDefaultContext() {
	Context ctx;
	ctx.iteration = vec4(0);
	return ctx;
}

struct MaterialContext {
	Sdf result;
	Context context;
};

Sdf opSimpleUnion(Sdf res1, Sdf res2){
	return (res1.x<res2.x)? res1:res2;
}

float opSimpleUnion(float res1, float res2) {
	return min(res1, res2);
}

Sdf opSimpleIntersect(Sdf res1, Sdf res2) {
	return (res1.x>res2.x) ? res1 : res2;
}

float opSimpleIntersect(float res1, float res2) {
	return max(res1, res2);
}

Sdf opSimpleDiff(Sdf res1, Sdf res2) {
	Sdf res = res1;
	res.x = max(-res1.x, res2.x);
	return res;
}

float opSimpleDiff(float res1, float res2) {
	return max(-res1, res2);
}

Sdf opSmoothUnionM(Sdf d1, Sdf d2, float k) {
	float h = clamp(0.5 + 0.5*(d2.x-d1.x)/k, 0.0, 1.0);
	float resx = mix(d2.x, d1.x, h) - k*h*(1.0-h);
	Sdf res = d1;
	res.x = resx;
	res.material = d2.material;
	res.material2 = d1.material;
	res.interpolant = h;
	res.refract = d1.refract || d2.refract;
	res.reflect = d1.reflect || d2.reflect;
	return res;
}

float opSmoothUnionM(float d1, float d2, float k) {
	float h = clamp(0.5 + 0.5*(d2-d1)/k, 0.0, 1.0);
	return mix(d2, d1, h) - k*h*(1.0-h);
}

mat3 rotateMatrix(vec3 r) {
	return TDRotateOnAxis(r.x, vec3(1, 0, 0)) *
		TDRotateOnAxis(r.y, vec3(0, 1, 0)) *
		TDRotateOnAxis(r.z, vec3(0, 0, 1));
}

int quadrantIndex(ivec2 cell) {
	/*
	[0] -1, 1    [1] 1, 1
	[2] -1, -1   [3] 1, -1
	*/
	return (((cell.y + 1) / 2) * 2) + ((cell.x + 1) / 2);
}

// https://github.com/msfeldstein/glsl-map/blob/master/index.glsl

float mapRange(float value, float inMin, float inMax, float outMin, float outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec2 mapRange(vec2 value, vec2 inMin, vec2 inMax, vec2 outMin, vec2 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec3 mapRange(vec3 value, vec3 inMin, vec3 inMax, vec3 outMin, vec3 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec4 mapRange(vec4 value, vec4 inMin, vec4 inMax, vec4 outMin, vec4 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

float modZigZag(float p) {
	float modded = mod(p, 2.);
	if (modded > 1) {
		return 2 - modded;
	}
	return modded;
}

vec2 modZigZag(vec2 p) {
	vec2 modded = mod(p, 2.);
	return vec2(
		modded.x > 1 ? (2 - modded.x) : modded.x,
		modded.y > 1 ? (2 - modded.y) : modded.y);
}

vec4 modZigZag(vec4 p) {
	vec4 modded = mod(p, 2.);
	return vec4(
		modded.x > 1 ? (2 - modded.x) : modded.x,
		modded.y > 1 ? (2 - modded.y) : modded.y,
		modded.z > 1 ? (2 - modded.z) : modded.z,
		modded.w > 1 ? (2 - modded.w) : modded.w);
}

float modZigZag(float p, float low, float high) {
	p -= low;
	float range = high - low;
	float modded = mod(p, range * 2.);
	if (modded > range) {
		return low + (range * 2. - modded);
	}
	return low + modded;
}

vec4 modZigZag(vec4 p, vec4 low, vec4 high) {
	p -= low;
	vec4 range = high - low;
	vec4 range2 = range * 2.;
	vec4 modded = mod(p, range2);
	return low + vec4(
		modded.x > range.x ? (range2.x - modded.x): modded.x,
		modded.y > range.y ? (range2.y - modded.y): modded.y,
		modded.z > range.z ? (range2.z - modded.z): modded.z,
		modded.w > range.w ? (range2.w - modded.w): modded.w);
}
