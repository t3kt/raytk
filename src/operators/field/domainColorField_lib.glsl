// https://github.com/rreusser/glsl-hypot
float domcol_hypot (vec2 z) {
	float t;
	float x = abs(z.x);
	float y = abs(z.y);
	t = min(x, y);
	x = max(x, y);
	t = t / x;
	return (z.x == 0.0 && z.y == 0.0) ? 0.0 : x * sqrt(1.0 + t * t);
}

vec4 domainColoring (vec2 z, vec2 gridSpacing, float saturation, float gridStrength, float magStrength, float linePower) {
	float carg = atan(z.y, z.x);
	float cmod = domcol_hypot(z);

	float rebrt = (fract(z.x / gridSpacing.x) - 0.5) * 2.0;
	rebrt *= rebrt;

	float imbrt = (fract(z.y / gridSpacing.y) - 0.5) * 2.0;
	imbrt *= imbrt;

	float grid = 1.0 - (1.0 - rebrt) * (1.0 - imbrt);
	grid = pow(abs(grid), linePower);

	float circ = (fract(log2(cmod)) - 0.5) * 2.0;
	circ = pow(abs(circ), linePower);

	circ *= magStrength;

	vec3 rgb = TDHSVToRGB(vec3(carg * 0.5 / PI, saturation, 0.5 + 0.5 * saturation - gridStrength * grid));
	rgb *= (1.0 - circ);
	rgb += circ * vec3(1.0);
	return vec4(rgb, 1.0);
}