// https://www.shadertoy.com/view/tcfGWB
// 3D Sierpinski Dodecahedron - SDF by TheArchCoder

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	vec3 n1 = normalize(vec3(-1.0, GOLDEN_RATIO - 1.0, 1.0 / (GOLDEN_RATIO - 1.0)));
	vec3 n2 = normalize(vec3(GOLDEN_RATIO - 1.0, 1.0 / (GOLDEN_RATIO - 1.0), -1.0));
	vec3 n3 = normalize(vec3(1.0 / (GOLDEN_RATIO - 1.0), -1.0, GOLDEN_RATIO - 1.0));
	float scale;
	float orbit_trap = 100000.0;
	float r2;
	vec3 offset = THIS_Offset;
	int i = 0;
	int iterations = int(THIS_Iterations);

	for (; i < 30; i++) {
		if (i >= iterations) break;

		p -= 2.0 * min(0.0, dot(p, n1)) * n1;
		p -= 2.0 * min(0.0, dot(p, n2)) * n2;
		p -= 2.0 * min(0.0, dot(p, n3)) * n3;
		p -= 2.0 * min(0.0, dot(p, n1)) * n1;
		p -= 2.0 * min(0.0, dot(p, n2)) * n2;
		p -= 2.0 * min(0.0, dot(p, n3)) * n3;
		p -= 2.0 * min(0.0, dot(p, n1)) * n1;
		p -= 2.0 * min(0.0, dot(p, n2)) * n2;
		p -= 2.0 * min(0.0, dot(p, n3)) * n3;

		#ifdef THIS_EXPOSE_step
		THIS_step = n;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(iterations - 1);
		#endif
		#ifdef THIS_HAS_INPUT_scaleField
		scale = inputOp_scaleField(p0, ctx);
		#else
		scale = THIS_Scale;
		#endif
		vec3 offset = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		offset += inputOp_offsetField(p0, ctx).xyz;
		#endif

		p = p * scale - offset * (scale - 1.0);

		r2 = dot(p, p);
		orbit_trap = min(orbit_trap, abs(r2));
		if (r2 > 64.0) break;
	}

	float d = 0.99 * length(p) * pow(scale, float(-i - 1));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit_trap, 0., 0., 0.);
	#endif
	return res;
}