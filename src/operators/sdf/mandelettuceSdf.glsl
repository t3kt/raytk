// Based on 3D Mandelettuce Fractal by TheArchCoder https://www.shadertoy.com/view/tflSzn

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;

	float orbitTrap = 1000.0;
	int n = int(THIS_Iterations);
	float dr = 1.0;
	float r = length(p);
	for (int i = 0; i < n; i++) {
		if (r > 20.0) break;
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#endif
		dr = dr * 2.0 * r;
		float psi = abs(mod(atan(p.z, p.y) + PI / 8.0, PI / 4.0) - PI / 8.0);
		p.yz = vec2(cos(psi), sin(psi)) * length(p.yz);
		vec3 p2 = p * p;
		vec3 offset = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		offset += inputOp_offsetField(p0, ctx).xyz;
		#endif
		p = vec3(vec2(p2.x - p2.y, 2.0 * p.x * p.y) * (1.0 - p2.z / (p2.x + p2.y + p2.z)),
			2.0 * p.z * sqrt(p2.x + p2.y)) + offset;
		r = length(p);

		orbitTrap = min(orbitTrap, dot(p, p));
	}
	Sdf res = createSdf(min(0.5 * log(r) * r / max(dr, 1.0), 1.0));
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbitTrap, 0., 0., 0.);
	#endif
	return res;
}