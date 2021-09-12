// modZigZag.glsl

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

vec3 modZigZag(vec3 p) {
	vec3 modded = mod(p, 2.);
	return vec3(
	modded.x > 1 ? (2 - modded.x) : modded.x,
	modded.y > 1 ? (2 - modded.y) : modded.y,
	modded.z > 1 ? (2 - modded.z) : modded.z);
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

vec2 modZigZag(vec2 p, vec2 low, vec2 high) {
	p -= low;
	vec2 range = high - low;
	vec2 range2 = range * 2.;
	vec2 modded = mod(p, range2);
	return low + vec2(
	modded.x > range.x ? (range2.x - modded.x): modded.x,
	modded.y > range.y ? (range2.y - modded.y): modded.y);
}

vec3 modZigZag(vec3 p, vec3 low, vec3 high) {
	p -= low;
	vec3 range = high - low;
	vec3 range2 = range * 2.;
	vec3 modded = mod(p, range2);
	return low + vec3(
	modded.x > range.x ? (range2.x - modded.x): modded.x,
	modded.y > range.y ? (range2.y - modded.y): modded.y,
	modded.z > range.z ? (range2.z - modded.z): modded.z);
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
