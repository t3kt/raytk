#ifndef CUBEHELIX
#define CUBEHELIX
vec3 cubehelix(vec3 c) {
	vec2 sc = vec2(sin(c.x), cos(c.x));
	return c.z * (1.0 + c.y * (1.0 - c.z) * (
	sc.x * vec3(0.14861, 0.29227, -1.97294) +
	sc.y * vec3(1.78277, -0.90649, 0.0)
	));
}
#endif
ReturnT thismap(CoordT p, ContextT ctx) {
	p += THIS_Phase;
	return vec4(cubehelix(vec3(
	TAU * p - 1.74533,
	(0.25 * cos(TAU * p) + 0.25) * vec2(-1.5, -0.9) + vec2(1.5, 0.8)
	)), 0.);
}