// https://www.shadertoy.com/view/wcX3WB
// 3D Sierpinski Icosahedron - SDF by TheArchCoder

ReturnT thismap(CoordT p, ContextT ctx) {
	int iterations = int(THIS_Iterations);
	float power = THIS_Power;
	float scale = power;
	vec3 n1 = normalize(vec3(-GOLDEN_RATIO, GOLDEN_RATIO - 1.0, 1.0));
	vec3 n2 = normalize(vec3(1.0, -GOLDEN_RATIO, GOLDEN_RATIO + 1.0));
	vec3 n3 = normalize(vec3(0.0, 0.0, -1.0));
	vec3 offset = THIS_Offset;
	float orbit_trap = 100000.0;
	float r;
	float t;
	int n = 0;
	p = abs(p);
	t = dot(p, n1); if (t > 0.0) p -= 2.0 * t * n1;
	t = dot(p, n2); if (t > 0.0) p -= 2.0 * t * n2;
	t = dot(p, n3); if (t > 0.0) p -= 2.0 * t * n3;
	t = dot(p, n2); if (t > 0.0) p -= 2.0 * t * n2;

	for (; n < iterations; n++) {
		p = abs(p);
		t = dot(p, n1); if (t > 0.0) p -= 2.0 * t * n1;
		p = scale * p - offset * (scale - 1.0);

		r = dot(p, p);
		orbit_trap = min(orbit_trap, abs(r));
		if (r > 64.0) break;
	}
	float d = length(p) * pow(scale, float(-n - 1));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit_trap, 0., 0., 0.);
	#endif
	return res;
}